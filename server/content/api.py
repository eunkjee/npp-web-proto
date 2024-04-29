import json

import requests
from comm.db import get_db_auto_close
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from utils.func import ResponseHandler

import numpy as np
from fitter import Fitter, get_common_distributions, get_distributions
from scipy import stats
import pylab

router = APIRouter(prefix="/content")


@router.get("/common2")
def test():
    response_handler = ResponseHandler()

    res = requests.get("http://127.0.0.1:8888/content/common2")
    response = json.loads(res.text)

    print(response)

    return response_handler.get_response()


@router.post("/common")
def winbugs(request: dict):
    response_handler = ResponseHandler()
    print(">>>>> api call")

    data = json.loads(request["data"])

    print(data)

    res = requests.post("http://127.0.0.1:8888/content/common", json=data)
    response = json.loads(res.text)

    print(response)

    print(response[1])

    resultList = []
    for data in response[1]:
        if data["defect.type"] == "PFD":
            resultList.append(data["value"])
    print("---------------pfd-----------------")
    print(resultList)

    values = np.array(resultList)

    # using Fitter library
    f = Fitter(values,
            xmin = 0,
            xmax = 1,
            # timeout = 60,
            # distributions = get_distributions())
            # distributions = get_common_distributions())
            distributions = ["beta",
                             "uniform"])
    print(f.fit())
    print(f.summary())

    # print(f.get_best(method = "aic"))
    # print(f.get_best(method = "bic"))
    # print(f.get_best(method = "sumsquare_error"))
    # print(f.get_best(method = "ks_statistic"))
    # print(f.get_best(method = "ks_pvalue"))

    print(f.fitted_param["beta"])
    print(f.fitted_param["uniform"])

    # using scipy library
    # fix loc=0 and scale=1
    beta = stats.beta

    trim_data = values[np.logical_and(values > 0, values < 1)]
    # print(trim_data)

    a1, b1, loc1, scale1 = beta.fit(trim_data
                            # , bounds={'a': (0,0), 'b': (1,1)}
                            , floc=0, fscale=1
                            )
    print(a1, b1, loc1, scale1)

    y, x = np.histogram(trim_data, bins=100, density=True)
    x = [(this + x[i + 1]) / 2.0 for i, this in enumerate(x[0:-1])]

    pdf_fitted = {}
    sq_error = {}

    pdf_fitted["beta"] = beta.pdf(x, a1, b1, loc1, scale1)
    pdf_fitted["uniform"] = stats.uniform.pdf(x)

    # calculate error
    sq_error["beta"] = pylab.sum((pdf_fitted["beta"] - y) ** 2)
    sq_error["uniform"] = pylab.sum((pdf_fitted["uniform"] - y) ** 2)
    print(sq_error)

    return response
