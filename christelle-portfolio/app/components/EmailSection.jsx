"use client";
import React, { useState } from 'react'
import Link from "next/link"
import Image from "next/image"

const EmailSection = () => {
    const [emailSubmitted, setEmailSubmitted] = useState(false);
    const handleSubmit = async (e) => {
        e.preventDefault();
        const data = {
            email: e.target.email.value,
            subject: e.target.subject.value,
            message: e.target.message.value
        }
        const JSONdata = JSON.stringify(data);
        const endpoint = "/api/send";

        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSONdata,
        };

        try {
                const response = await fetch(endpoint, options);
                
                if (response.ok) {
                    console.log("Message sent.");
                    setEmailSubmitted(true);
                } else {
                    console.error("Failed to send email.");
                }
            } 
        catch (error) {
                console.error("An error occurred while sending the email:", error);
            }
        };
    
  return (
    <section id ="contact" className ="grid md:grid-cols-2 my-12 md:my-12 py-24 gap-4 relative">
        <div className="bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-purple-900 to-transparent rounded-full h-80 w-80 z-0 blur-lg absolute top-3/4 -left-4 transform -translate-x-1/2 -translate-1/2">
        </div>
        <div className='z-10'>
            <h5>
                Let's Connect
            </h5>
            <p className='text-[#ADB7BE] mb-4 max-w-md'>
                {" "}
                Looking for opportunities in the tech field. Whether you 
                have any questions for me or just want to drop by and
                say hi, send a message and I'll get back to you!
            </p>

            <div className='socials flex flex-row gap-2'>
                <Link href ="https://www.linkedin.com/in/christelle-ridad-tech/">
                    <Image src="/images/linkedin-image.png"  alt="Linkedin Icon" width={30} height={30} />
                </Link>
            </div>
        </div>

        <div>
            <form className ="flex flex-col" onSubmit={handleSubmit}>
                <div className='mb-6'>
                    <label htmlFor="email" type="email" className='text-white' blick mb-2 text-sm font-medium>Enter your email
                        <input 
                        name="email"
                        type="email" 
                        id="email" 
                        required 
                        className='bg-[#18191E] border border-[#33353F] placeholder-[#9CA2A9] text-gray-100 text-sm rounded-lg block w-full p-2.5'
                        placeholder="your-email.gmail.com"/>
                    </label>
                </div>
                
                <div className='mb-6'>
                    <label htmlFor="subject" type="subject" className='text-white' blick mb-2 text-sm font-medium>Subject
                        <input 
                        name="subject"
                        type="subject" 
                        id="subject" 
                        required 
                        className='bg-[#18191E] border border-[#33353F] placeholder-[#9CA2A9] text-gray-100 text-sm rounded-lg block w-full p-2.5'
                        placeholder="I have a question"/>
                    </label>

                </div>
                
                <div className='mb-6'>
                    <label htmlFor="message" type="subject" className='text-white' blick mb-2 text-sm font-medium>Message
                        <textarea 
                        name="message"
                        type="message" 
                        id="message" 
                        required 
                        className='bg-[#18191E] border border-[#33353F] placeholder-[#9CA2A9] text-gray-100 text-sm rounded-lg block w-full p-2.5'
                        placeholder="Hey Christelle, I was wondering if..."
                        />
                    </label>

                </div>

                <button
                type ="submit"
                className='bg-purple-500 hover:bg-purple-600 text-white font-medium py-2.5 px-5 rounded-lg w-full'>
                    Send Message
                </button>
                {
                    emailSubmitted && (
                        <p className='text-green-500 text-sm mt-2'>
                            Email sent successfuly!
                        </p>
                    )
                }
            </form>
        </div>
    </section>
  )
}

export default EmailSection
