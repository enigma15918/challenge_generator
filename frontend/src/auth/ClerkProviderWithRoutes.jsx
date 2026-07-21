import {ClerkProvider} from "@clerk/clerk-react";
import {BrowserRouter} from "react-router-dom";
import "react"
const PUBLISHABLE_KEY= import.meta.env.VITE_PUBLIC_CLERK_PUBLISHABLE_KEY

if(!PUBLISHABLE_KEY){
  throw new Error("Missing Publishable Key")
}

export default function ClerkProviderWithRoutes({children}){

    return (
        <ClerkProvider publishableKey={PUBLISHABLE_KEY}>

            <BrowserRouter>{children}</BrowserRouter>

        </ClerkProvider>
    )


}