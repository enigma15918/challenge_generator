import "react"
import {useState,useEffect} from "react"
import MCQChallenge from "./MCQChallenge.jsx"


export default function ChallengeGenerator(){

    const [challenge,setChallenge]=useState(null)

    const [isLoading,setIsLoading]=useState(false)

    const [error,setError]=useState(null)

    const [difficulty,setDifficulty]=useState("easy")

    const [qouta,setQouta]=useState(null)

    const fetchQouta =async() => {}

    const generateChallenge = async () => {}

    const getNextResetTime= () => {}

    return <div className="challenge-container">

            <h2>Coding Challenge Generator</h2>

            <div className="qouta-display">

                <p>Challenge remaining tody : {qouta?.qouta_remaining || 0}</p>

                {qouta?.qouta_remaining === 0 && (
                    <p>Next reset : {0}</p>
                )}

            </div>

            <div className="difficulty-selector">
                <label htmlFor="difficulty">
                    Select Difficulty
                </label>

                <select  
                         id="difficulty"
                         value={difficulty}
                         onChange={(e)=>setDifficulty(e.target.value)}
                         disabled={isLoading}
                
                
                >

                    <option value="easy">Easy</option>
                    <option value="medium">Medium</option>
                    <option value="hard">Hard</option>

                </select>

            </div>
            
            <button

                onClick={generateChallenge}

                disabled={isLoading || qouta?.qouta_remaining ===0}

                className="generate-button"
            
            >

                {isLoading? "Generate....." : "Generate Challenge"}
                
            </button>


            {error && <div className="error-message">
                
                <p>{error}</p>
                
                </div>}

                {challenge && <MCQChallenge challenge={challenge}/>}

    </div>

}