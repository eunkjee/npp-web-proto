import './globals.css'
import classes from "./page.module.css";
import Image from "next/image";
import backgroundImg from "../../public/img/home-bg.png";

export const metadata = {
  title: 'npp-web-proto',
  description: 'description',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <Image className={classes.background} src={backgroundImg} alt="img" fill />
        {children}
      </body>
    </html>
  )
}
