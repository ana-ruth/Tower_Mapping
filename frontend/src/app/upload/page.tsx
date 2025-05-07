"use client"
import {useState} from "react";

export default function UploadFile(){

    const [files, setFiles] = useState<File[]>([]);

    const handleFileInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setFiles(Array.from(event.target.files || []));
    }

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        const formData = new FormData();
        files.forEach(file => {
            formData.append('file_uploads', file)
        })

        try{
            const endpoint = "http://localhost:8000/uploadfile/"
            const response = await fetch(endpoint, {
                method: "POST", 
                body: formData
            });
            
            if (response.ok){
                console.log("Files uploaded sucessfully!");
            }
            else{
                console.error("Failed to upload files.");
            }
        } catch(error){
            console.error(error);
        }
    }

    return (
        <div>
            <h1>Upload file</h1>
            <form onSubmit = {handleSubmit}>
                <div style = {{marginBottom: "20px"}}>
                    <input type="file" onChange= {handleFileInputChange} accept=".csv, .xlsx, .xls, .json" multiple/>
                </div>
                <button type = "submit">Upload</button>
            </form>

        </div>
    )
}

