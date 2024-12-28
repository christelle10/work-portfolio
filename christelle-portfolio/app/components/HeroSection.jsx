"use client"
import React from 'react';
import Image from "next/image"
import { TypeAnimation } from 'react-type-animation'
const HeroSection = () => {
  return (
    <section>
        <div className='grid grid-cols-1 sm:grid-cols-12'>
            <div className= 'col-span-7 place-self-center text-center sm:text-left'>
                
                  <h1 className ="text-white mb-4 text-4xl sm:text-5xl lg:text-6xl font-extrabold">
                    <span className='text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-600'>
                      Hi, I'm Telle. I'm a{" "}
                    </span>
                    <br></br>
                    <TypeAnimation
                        sequence={[
                          // Same substring at the start will only be typed out once, initially
                          'Software Developer',
                          1000, // wait 1s before replacing "Mice" with "Hamsters"
                          'UI Designer',
                          1000,
                          'Marketing Specialist',
                          1000,
                          'Team Player',
                          1000,

                        ]}
                        wrapper="span"
                        speed={50}
                        style={{ fontSize: '1em', display: 'inline-block' }}
                        repeat={Infinity}
                      />
                    </h1>
                  
                <p className = "text-[#ADB7BE] text-base sm:text-lg mb-6 lg:text-xl">
                    Welcome to my page 👋🏼
                </p>
                <div>
                  <button onClick={() => window.location.href = 'https://www.linkedin.com/in/christelle-ridad-tech/'} className='px-6 py-3 w-full sm:w-fit rounded-full mr-4 bg-gradient-to-br from-blue-500 via-purple-500 to-pink-500 bg-white hover:bg-slate-200 text-white'>Hire Me</button>
                  <button onClick={() => window.location.href = 'https://drive.google.com/file/d/14Mg3n3KBatMUJEuPa87Vw0KYHP1e8haV/view?usp=sharing'} className='px-1 py-1 w-full sm:w-fit mt-5 rounded-full bg-gradient-to-br from-blue-500 via-purple-500 to-pink-500 mr-4 bg-transparent hover:bg-slate-800 text-white'>
                    <span className="block bg-[#121212] hover:bg-slate-800 rounded-full px-5 py-2">Preview Resume</span>
                  </button>
                </div>
            </div>
            <div className = "col-span-5 place-self-center mt-4 lg:mt-0">
              <div className = "rounded-full bg-[#181818] w-[250px] h-[250px] lg:w-[400px] lg:h-[400px] relative">
                <Image 
                src ="/images/hero-image.png"
                alt="hero image"
                className='absolute transform -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'
                width={300}
                height={300}
                />
              </div>
                
            </div>
        </div>
        
    </section>
    
  )
}

export default HeroSection
