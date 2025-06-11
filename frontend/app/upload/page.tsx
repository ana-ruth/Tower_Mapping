
"use client"
import { useState, useCallback } from "react";
import { useDropzone } from "react-dropzone";

export default function UploadFile(){

    const [files, setFiles] = useState<File[]>([]);


    const onDrop = useCallback((acceptedFiles: File[]) => {
        setFiles(prevFiles => [...prevFiles, ...acceptedFiles]);

    }, []);

    const { getRootProps, getInputProps, isDragActive } = useDropzone({
        onDrop, 
        accept: {
        "application/vnd.ms-excel": [".xls"],
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": [".xlsx"],
        "application/json": [".json"],
        "text/csv": [".csv"],
    },
    multiple: true,
    });



    //process files
    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        const formData = new FormData();
        files.forEach(file => {
            formData.append('file_uploads', file)
        })

        try{
            const endpoint = "https://towermapping-h8ecgsdghyegfwbx.canadacentral-01.azurewebsites.net/uploadfile/"
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
        <div className="m-20">
            <h1 className = "text-5xl mb-15 ">Upload Excel Files</h1>
            <form onSubmit = {handleSubmit}>

                <div 
                    {...getRootProps()} 
                    className="border-5 border-dashed border-gray-400 rounded-xl p-12 w-[80vh] hover:bg-gray-200 flex flex-col items-center"
                >
                    
                    <input {...getInputProps()} />
                    
                        {/*Upload icon*/}
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="gray" className="size-15">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M3 16.5v2.25A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75V16.5m-13.5-9L12 3m0 0 4.5 4.5M12 3v13.5" />
                        </svg>
    
                        {
                            isDragActive ?
                            <p className ="text-gray-700 text-xl">Drop the files here ...</p> :
                            <p className ="text-gray-700 text-xl">Drag and drop files here, or <strong>browse</strong></p>
                        } 
               
                </div>

                <button type = "submit" className = "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg mt-15 ">Upload</button>
            </form>

        </div>
    )
}

