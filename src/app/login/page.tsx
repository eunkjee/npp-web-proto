import classes from "./page.module.css"

export default function LoginPage() {
    return (
        <div className={classes.container}>
            <div className={classes.wrapper}>
                <h1>Logo</h1>

                <div className={classes.inp}>
                    <input type={"text"} placeholder={"Username"}/>
                </div>
                <div className={classes.inp}>
                    <input type={"password"} placeholder={"Password"}/>
                </div>

                <button className={classes.btn} type={"submit"}>Sign In</button>

                <div className={classes.register}>
                    <p>Dont have an account?</p>
                </div>
            </div>
        </div>
    )
}