import Link from 'next/link';
import Image from "next/image";


export default function NavLinks() {
    
    return (
      <div className="flex justify-around ">
            <div className = " flex row basis-3/4">
                <Image
                aria-hidden
                src="/window.svg"
                alt="Window icon"
                width={16}
                height={16}
                />
                <Link href="/" className=" text-xl p-6  ">Tower Mapping</Link>
            </div>

        <div className = "flex row">
            <Link href = "/upload" className = "text-lg basis-1/2 p-6">Upload</Link>
            <Link href ="/map" className=" text-lg basis-1/2 p-6 hover:underline hover:underline-offset-4">Status</Link>
            <Link href = "/" className = "text-lg basis-1/2 p-6">Report</Link>
        </div>

      </div>
        
      )
  }