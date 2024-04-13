<a name="readme-top"></a>


<!-- PROJECT LOGO -->
<div align="center">
  <img src="https://cdn.discordapp.com/attachments/1208842676259258380/1228653360379334676/angelic.png?ex=662cd39c&is=661a5e9c&hm=f85bbce57918b72364ae720e77dbec517a06355d1c3e76da868931de6053754d&" alt="Logo" width="200" height="200">
  <h1 align="center">Angelic: Code with No brain</h1>
</div>




<!-- TABLE OF CONTENTS -->
<details>
  <summary>🗂️ Table of Contents</summary>
  <ol>
    <li><a href="#-mission">🎯 Our Mission</a></li>
    <li><a href="#-what-is-devin">🤔 What is Devin?</a></li>
    <li><a href="#-why-Angelic">🐚 Why We are here?</a></li>
    <li><a href="#-project-status">🚧 Project Stats</a></li>
      <a href="#-get-started">🚀 Getting  Started</a>
      <ul>
        <li><a href="#1-requirements">1. Requirements</a></li>
        <li><a href="#2-build-and-setup">2. Build and Setup</a></li>
        <li><a href="#3-run-the-application">3. Run the Application</a></li>
        </li>
      </ul>
    </li>
    <li><a href="#%EF%B8%8F-research-strategy">⭐️ Research Strategy</a></li>
    <li><a href="#-how-to-contribute">🤝 How to Contribute</a></li>
    <li><a href="#-join-our-community">🤖 Join Our Community</a></li>
    <li><a href="#%EF%B8%8F-built-with">🛠️ Built With</a></li>
    <li><a href="#-license">📜 License</a></li>
  </ol>
</details>

## 🎯 Our Mission
**This Demo video , The time when it was recorded there were small bugs and in this release its already fixed.**

[Project Demo Video](./demo7_1.mp4)


Angelic is an advanced AI software engineer that can understand the programmers's instructions and then , breaking it down\ into smaller yet optimal steps, research relevant information needed to write bug free and optimal code. Angelic uses large language models (LLM'S) for planning and reasoning algorithms, and web browsing abilities are developed into the it to give the best result out.

<p align="right" style="font-size: 14px; color: #555; margin-top: 20px;">
    <a href="#readme-top" style="text-decoration: none; color: #007bff; font-weight: bold;">
        ↑ Back to Top ↑
    </a>
</p>

## 🤔 What is Devin?
Devin represents a cutting-edge autonomous agent designed to navigate the complexities of software engineering. It leverages a combination of tools such as a shell, code editor, and web browser, showcasing the untapped potential of LLMs in software development. Our goal is to explore and expand upon Devin's capabilities, identifying both its strengths and areas for improvement, to guide the progress of open code models.

<p align="right" style="font-size: 14px; color: #555; margin-top: 20px;">
    <a href="#readme-top" style="text-decoration: none; color: #007bff; font-weight: bold;">
        ↑ Back to Top ↑
    </a>
</p>

## 🐚 Why Angelic?
The Angelic Project is conceived from a deep-rooted ambition to not just replicate but to elevate and innovate beyond the foundational Devin model. With a profound commitment to collaboration with the open-source community, our mission is to confront and surmount the hurdles encountered by Code LLMs in real-world applications. Our endeavor is to craft solutions that not only substantially benefit the community but also serve as stepping stones for the evolution of the field.

<p align="right" style="font-size: 14px; color: #555; margin-top: 20px;">
    <a href="#readme-top" style="text-decoration: none; color: #007bff; font-weight: bold;">
        ↑ Back to Top ↑
    </a>
</p>

## 🚧 Project Status

Angelic' is presently in its alpha stage, continuously evolving towards its full potential. You're welcome to explore the alpha version to witness our ongoing progress and experience the end-to-end results firsthand. Our dedicated project team is fervently engaged in advancing towards the following key milestones:

1. **UI**: The Angelic Project is committed to crafting a user-friendly interface that seamlessly integrates various components, including a chat interface, a shell for demonstrating commands, and a web browser. Our goal is to provide a cohesive and intuitive user experience that empowers users to interact with the agent effortlessly across different mediums. By prioritizing usability and accessibility, we aim to democratize access to AI technology and foster greater collaboration and innovation within the community..

2. **Architecture**: The Angelic Project is dedicated to constructing a resilient agent framework with a robust backend capable of seamlessly handling tasks such as reading, writing, and executing simple commands. Our focus is on creating a stable foundation that empowers the agent to interact with its environment effectively and reliably. By prioritizing stability and reliability in our framework, we aim to facilitate smoother and more efficient operations, laying the groundwork for further advancements in AI technology.

3. **Agent Capabilities**: The Angelic Project is dedicated to amplifying the agent's prowess in generating bash scripts, executing tests, and mastering various software engineering tasks that remain unattainable for other models. Our focus lies in pushing the boundaries of capability, enabling the agent to tackle challenges with finesse and precision, thereby unlocking new horizons in the realm of artificial intelligence and software development.
- **Evaluation**: The Angelic Project is setting the foundation for a streamlined evaluation pipeline that not only aligns with Devin's criteria but also extends beyond it. Our aim is to establish a robust framework that ensures consistency in assessment while also encompassing additional dimensions of performance and utility. Through this minimal evaluation pipeline, we seek to provide a comprehensive and insightful analysis of the agent's capabilities, enabling a deeper understanding of its strengths and areas for improvement.

Following the achievement of the aforementioned milestones, the Angelic project team will pivot towards intensive research in diverse areas:

<p align="right" style="font-size: 14px; color: #555; margin-top: 20px;">
    <a href="#readme-top" style="text-decoration: none; color: #007bff; font-weight: bold;">
        ↑ Back to Top ↑
    </a>
</p>

## 🚀 Get Started

Getting started with the Angelic project is incredibly easy. Follow these simple steps to set up and run Angelic on your system:

### 1. Requirements
* Linux, Mac OS, or [WSL on Windows](https://learn.microsoft.com/en-us/windows/wsl/install)
* [Python](https://www.python.org/downloads/) >= 3.11
* [NodeJS](https://nodejs.org/en/download/package-manager) >= 18.17.1

### 2. Build and Setup The Environment

- **Build the Project:** Begin by building the project, which includes setting up the environment and installing dependencies. This step ensures that Angelic is ready to run smoothly on your system.
    ```bash
    pip install -r requirements.txt
    
    playwright install 

    playwright install --with-deps
    
    cd ui

    playwright install --with-deps
    ```

### 3. Configuring the Language Model

Angelic supports a diverse array of Language Models (LMs) through the powerful. By default, we've chosen the mighty GPT-4 from OpenAI as our go-to model, but the world is your oyster! You can unleash the potential of Anthropic's suave Claude, the enigmatic Llama, or any other LMM's that piques your interest.

To configure the LM of your choice, follow these steps:

1. **Using Sample.config.toml:**
   Find the sample.config.toml and rename it to config.toml and fill up the Api's to get the project to start working .

2. **Install Bun :** 
    Install bun as it is needed for the ui interface of the project. To install this follow the steps:

    ```bash
    Make sure you open your powershell windows in admin mode . Once done open copy and paste this code there:

    For windows :

    powershell -c "irm bun.sh/install.ps1|iex"
    
    set this as an env variable :C:\Users\<UserName>\.bun\bin

    For mac , Lunix , Wsl:

    curl -fsSL https://bun.sh/install | bash

    ```

3. **Installing Node Modules**: there are steps to install the node modules :

```bash
npm install

npm i playwright

npm i playwright-core
```



**Note on Alternative Models:**


### 4. Run the Application

- **Run the Application:** Once the setup is complete, launching Angelic is as simple as running a single command. This command starts both the backend and frontend servers seamlessly, allowing you to interact with Angelic without any hassle.


### 5. Individual Server Startup

- **Start the Backend Server:** If you prefer, you can start the backend server independently to focus on backend-related tasks or configurations.
    ```bash
    python angelic.py
    ```

- **Start the Frontend Server:** Similarly, you can start the frontend server on its own to work on frontend-related components or interface enhancements.
    ```bash
    cd ui

    bun run dev

    if any errors comes try setting this as as your env path : 
    
    C:\Program Files\Node-js\node_modules\corepack\shims\nodewin\ 

    ```


<p align="right" style="font-size: 14px; color: #555; margin-top: 20px;">
    <a href="#readme-top" style="text-decoration: none; color: #007bff; font-weight: bold;">
        ↑ Back to Top ↑
    </a>
</p>

## ⭐️ Research Strategy

Achieving full replication of production-grade applications with LLMs is a complex endeavor. Our strategy involves:

1. **Core Technical Research:** The project will pivot towards foundational research aimed at comprehensively understanding and refining the technical intricacies of code generation and manipulation. This endeavor will delve deep into the underlying principles governing code generation processes, seeking to advance methodologies and techniques to enhance the efficiency, accuracy, and adaptability of code handling mechanisms. By focusing on foundational research, we aim to lay a solid groundwork for further advancements in AI-driven code generation, fostering innovation and breakthroughs in this critical domain.

2. **Specialist Abilities:** The project will concentrate on amplifying the effectiveness of core components by refining data curation techniques, optimizing training methods, and exploring additional avenues for improvement. This initiative entails meticulous curation of datasets to ensure relevance and diversity, employing advanced training methodologies such as self-supervised learning and reinforcement learning to enhance model performance, and investigating novel techniques to address challenges and bottlenecks. By enhancing the effectiveness of core components, we strive to elevate the overall performance and capabilities of the system, ultimately delivering more robust and impactful solutions to real-world problems.

3. **Task Planning:** Advancing capabilities for bug detection, codebase management, and optimization strategies. This involves refining algorithms and tools to automatically identify and rectify bugs within codebases, implementing robust systems for efficient organization and navigation of code repositories, and devising optimization techniques to enhance performance and scalability. By bolstering task planning functionalities, we aim to streamline software development processes, mitigate risks, and improve the overall quality and maintainability of codebases.

4. **Evaluation:** Establishing comprehensive evaluation metrics to deepen our understanding and refine the performance of our models. This includes developing nuanced metrics that capture various aspects of model behavior, such as accuracy, efficiency, robustness, and ethical considerations. Additionally, we will design rigorous evaluation protocols and benchmarks to systematically assess model performance across diverse tasks and datasets. By establishing robust evaluation frameworks, we aim to drive continuous improvement and ensure that our models meet the highest standards of effectiveness and reliability.

<p align="right" style="font-size: 14px; color: #555; margin-top: 20px;">
    <a href="#readme-top" style="text-decoration: none; color: #007bff; font-weight: bold;">
        ↑ Back to Top ↑
    </a>
</p>

## 🤝 How to Contribute

Angelic is a community-driven project, and we welcome contributions from everyone. Whether you're a developer, a researcher, or simply enthusiastic about advancing the field of software engineering with AI, there are many ways to get involved:

- **Code Contributions:** Help us develop the core functionalities, frontend interface, or sandboxing solutions.
- **Research and Evaluation:** Contribute to our understanding of LLMs in software engineering, participate in evaluating the models, or suggest improvements.
- **Feedback and Testing:** Use the Angelic toolset, report bugs, suggest features, or provide feedback on usability and don't get shy from fixing the bugs out there 😅.



<p align="right" style="font-size: 14px; color: #555; margin-top: 20px;">
    <a href="#readme-top" style="text-decoration: none; color: #007bff; font-weight: bold;">
        ↑ Back to Top ↑
    </a>
</p>

## 🤖 Join Our Community

We will be soon launching our discord server . Once launched we would update it here.


<p align="right" style="font-size: 14px; color: #555; margin-top: 20px;">
    <a href="#readme-top" style="text-decoration: none; color: #007bff; font-weight: bold;">
        ↑ Back to Top ↑
    </a>
</p>

## 📜 License

Distributed under the MIT License. See [`LICENSE`](./LICENSE) for more information.

<p align="right" style="font-size: 14px; color: #555; margin-top: 20px;">
    <a href="#readme-top" style="text-decoration: none; color: #007bff; font-weight: bold;">
        ↑ Back to Top ↑
    </a>
</p>


