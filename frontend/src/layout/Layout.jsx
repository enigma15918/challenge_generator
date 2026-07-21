import {SignedIn,SignedOut,UserButton} from "@clerk/clerk-react"
import {Outlet,Link,Navigate} from "react-router-dom"
import "react"
export  function Layout(){
    return <div className="app-layout">

        <header className="app-header">

            <div className="header-content">

                <h1>Code Challenge Generator</h1>

                <nav>

                    <SignedIn>
                        <Link to="/">Generate Challenge</Link>
                        <Link to="/history">History</Link>
                        <UserButton/>
                    </SignedIn>
                    
                    {/* <SignedOut>

                    </SignedOut> */}

                </nav>


            </div>
        </header>

        <main className="app-main">
            <SignedOut>
                <Navigate to="/sign-in"/>

            </SignedOut>

            <SignedIn>
                <Outlet />
            </SignedIn>

        </main>

    </div>
}