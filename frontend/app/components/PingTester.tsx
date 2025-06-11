// Example: Fetching data in Next.js
async function getData() {
    const res = await fetch('https://towermapping-h8ecgsdghyegfwbx.canadacentral-01.azurewebsites.net/');
    const data = await res.json();
    return data;
  }
  
  export default async function Page() {
    const data = await getData();
    return (
      
        <h1>{data.ping}</h1>
      
    );
  }