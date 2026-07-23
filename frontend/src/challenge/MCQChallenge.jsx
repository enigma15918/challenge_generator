import "react"

import {useState} from "react"

export default function MCQChallenge({challenge,showExplaination=false}){

    const [selectedOption,setSelectedOption] = useState(null)

    const [shouldShowExplaination,setShouldShowExplaination] = useState(showExplaination)


    const  options= typeof challenge.options === "string" ? JSON.parse(challenge.options):challenge.options

    const handleOptionSelect = (index) =>{
        if (selectedOption !== null) return;
        setSelectedOption(index)
        setShouldShowExplaination(true)
    }

    const getOptionClass=(index)=>{

        if (selectedOption === null) return "option";

        if (index === Number(challenge.correct_answer_id)){
            return "correct option"
        }

        if (selectedOption === index && index !== challenge.correct_answer_id){
            return "option incorrect"
        }

        return "option"

    }
    console.log(challenge.explanation)
    return <div className="challenge-display">
        <p><strong>Difficulty</strong>:{challenge.difficulty}</p>
        <p className="challenge-title">{challenge.title}</p>


        <div className="options">

            {options.map((option,index) => (

                <div 
                className={getOptionClass(index)}
                         key={index}
                         onClick={() => handleOptionSelect(index)}


                
                >

                    {option}


                </div>

            ))}


        </div>

            {shouldShowExplaination && selectedOption !== null && (
                <div className="explanation" >

                    <h4>Explaination</h4>
                    <p>{challenge.explanation}</p>
                    

                </div>
            )}

    </div>

} 