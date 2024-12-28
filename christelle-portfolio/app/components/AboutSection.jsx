"use client"
import React, { useTransition, useState } from 'react';
import Image from "next/image"
import TabButton from './TabButton';

const TAB_DATA = [
    {
        title: "Skills",
        id: "skills",
        content: (
            <ul>
                <li>• Python, C++, JavaScript</li>
                <li>• SQL</li>
                <li>• HTML, CSS, React</li>
                <li>• Adobe Photoshop, Figma</li>
                <li>• Raspberry Pi, Arduino</li>
                <li>• Git Version Control</li>
            </ul>
        )
    },

    {
        title: "Education",
        id: "education",
        content: (
            <ul>
                <li>• FEU Institute of Technology, BS Computer Engineering</li>
                <li>• UE Caloocan, STEM Track</li>                
            </ul>
        )
    },

    {
        title: "Certifications",
        id: "certifications",
        content: (
            <ul>
                <li>• Google Digital Marketing and Ecommerce - 2023</li>
                <li>• CCNA: Switching, Routing, and Wireless Essentials - 2023</li>
                <li>• Freecodecamp: JavaScript Algorithms and Data Structures Developer Certification - 2023</li>
                <li>• AWS Academy Graduate - 2022</li>
                <li>• CCNA: Introduction to Networks - 2022</li>
                <li>• BayanAcademy: Advanced Front-End Web Development Training - 2022</li>
                <li>• Pearson: IT Specialist Python Certification - 2022</li>
                <li>• Freecodecamp: Responsive Web Design Developer Certification - 2021</li>
                
            </ul>
        )
    }
]

const AboutSection = () => {
    const [tab, setTab] = useState("skills");
    const [isPending, startTransition] = useTransition();

    const handleTabChange = (id) => {
        startTransition(() => {
            setTab(id);
        });
    };
  return <section className= "text-white">
    <div className='md:grid md:grid-cols-2 gap-8 items-center py-8 px-4 xl:gap-16 sm:py-16 xl:px-16'>
        <Image src = "/images/about-me.png" width = {500} height={500} />
        <div className = "mt-4 md:mt-0 text-left flex flex-col h-full">
            <h2 className = "text-4xl font-bold text-white mb-4">About Me</h2>
            <p className="text-base md:text-lg">I'm a dynamic professional with a strong background in programming, 
            UI design, and project management. Leading projects like the Ocu-Aspida Digital Eyestrain Detector 
            and Bangka Buddy has been both rewarding and challenging. With experience as a Social Media Marketing 
            Specialist, I also bring marketing skills to the table. I'm always open 
            to learning new skills and willing to collaborate on meaningful projects.
            </p>
            <div className = "flex flex-row at mt-8">
                <TabButton selectTab = {() => handleTabChange("skills")} active={tab === 'skills'}>
                    {" "}Skills{" "}
                </TabButton>

                <TabButton selectTab = {() => handleTabChange("certifications")} active={tab === 'certifications'}>
                    {" "}Certifications{" "}
                </TabButton>

                <TabButton selectTab = {() => handleTabChange("education")} active={tab === 'education'}>
                    {" "}Education{" "}
                </TabButton>
            </div>
            <div className ="mt-5">{TAB_DATA.find((t) => t.id === tab).content}</div>

            
        </div>

    </div>
  </section>
}

export default AboutSection
