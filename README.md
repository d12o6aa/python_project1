# Freelance System

Welcome to the Freelance System, a simple command-line interface project designed for both clients and freelancers to connect in the world of freelancing. This system allows users to register, login, post job opportunities, view freelancers, and interact with job proposals.

## Getting Started

### Prerequisites

- Python 3.x

### Running the Script

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/d12o6aa/python_project1.git
   ```

2. Navigate to the project directory:

   ```bash
   cd python_project1
   ```

3. Run the script:

   ```bash
   python freelance_system.py
   ```

4. Follow the on-screen prompts to interact with the Freelance System.

## Project Structure

- The system uses a directory structure to organize user and job information.
- For each client, a folder is created under 'the system/client' with a text file containing client details.
- For each job, a folder is created under 'the system/jop' with a text file containing job details and additional files for client and freelancer interaction.
- For each freelancer, a folder is created under 'the system/freelancer' with a text file containing freelancer details.

## User Roles

### Client

- **Registration:** Clients can register by providing a username, password, ID, and email.
- **Login:** Clients can log in using their credentials.
- **Job Management:**
  - **Add Job Post:** Clients can add a job post by entering the title, description, post ID, and a list of required skills.
  - **Remove Job Post:** Clients can remove a job post by providing the title of the post.
  - **View Freelancers:** Clients can view the list of freelancers available in the system.
  - **Manage Proposals:** Clients can check if freelancers have sent proposals for their job posts, accept or reject proposals, and update the system accordingly.

### Freelancer

- **Registration:** Freelancers can register by providing a username, password, ID, email, phone number, and national ID.
- **Login:** Freelancers can log in using their credentials.
- **Job Interaction:**
  - **View Accepted Jobs:** Freelancers can view the jobs they have been accepted for by clients.
  - **View Available Jobs:** Freelancers can view the list of available job posts in the system and choose to send proposals for jobs they are interested in.

## File Structure

- The system uses a directory structure to organize user and job information.
- For each client, a folder is created under 'the system/client' with a text file containing client details.
- For each job, a folder is created under 'the system/jop' with a text file containing job details and additional files for client and freelancer interaction.
- For each freelancer, a folder is created under 'the system/freelancer' with a text file containing freelancer details.

## Usage

1. Run the script and choose whether you are a client or a freelancer.
2. Follow the prompts to register or login.
3. Clients can manage job posts, view freelancers, and handle proposals.
4. Freelancers can view accepted jobs and available jobs, as well as send proposals for jobs.

Note: This project is a command-line interface and is intended for educational purposes. It provides a basic framework for a freelance system and can be expanded for more features and improvements.

---

**Repository Link:** [https://github.com/d12o6aa/python_project1](https://github.com/d12o6aa/python_project1)
