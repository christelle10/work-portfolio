"use client";
import React, { useState, useRef } from "react";
import ProjectCard from "./ProjectsCard";
//import ProjectTag from "./ProjectTag";
//import { motion, useInView } from "framer-motion";

const projectsData = [
  {
    id: 1,
    title: "Ocu-Aspida Digital Eyestrain Detector",
    description: "A final thesis project that detect if user is in risk of acquiring digital eyestrain while using their device. Tech Stack: Python, SQL, CustomTkinter and TTKBootstrap",
    image: "/images/projects/1.png",
    tag: ["All", "Web"],
    gitUrl: "/",
    previewUrl: "/",
  },
  {
    id: 2,
    title: "BangkaBuddy",
    description: "A pitching competition project that aims to help fishermen in increasing their catch, plot their routes, and maximize income.",
    image: "/images/projects/2.png",
    tag: ["All", "Web"],
    gitUrl: "/",
    previewUrl: "/",
  },
  {
    id: 3,
    title: "Mixtape-Me",
    description: "A software design project that creates a mixtape based on user's Spotify data which they can post on their social media account.",
    image: "/images/projects/3.png",
    tag: ["All", "Web"],
    gitUrl: "/",
    previewUrl: "/",
  },
  {
    id: 4,
    title: "CashMate",
    description: "A single-page React app to track your expenses and income with visualizations.",
    image: "/images/projects/4.png",
    tag: ["All", "Mobile"],
    gitUrl: "/",
    previewUrl: "/",
  },
  {
    id: 5,
    title: "Netflix Lite",
    description: "A final project for a Front End Web Dev bootcamp. It's a Netflix Clone web app that dynamically changes movie and series data from actual Netflix site.",
    image: "/images/projects/5.png",
    tag: ["All", "Web"],
    gitUrl: "/",
    previewUrl: "/",
  },

];

const ProjectsSection = () => {


  return (
    <section id="projects">
      <h2 className="text-center text-4xl font-bold text-white mt-4 mb-8 md:mb-12">
        My Projects
      </h2>
      <div>
        {projectsData.map((project) => (
          <ProjectCard
            key={project.id}
            title={project.title}
            description={project.description}
            imgUrl={project.image}
            gitUrl={project.gitUrl}
            previewUrl={project.previewUrl}
            tags={project}
          />
        ))}
      </div>
    </section>
  );
};

export default ProjectsSection;