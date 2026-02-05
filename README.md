# 📺🍿 Personalisation for (Public) Media (INFOMPPM) 📡🎬
Welcome to the tutorials repository for the Personalisation for (Public) Media course. Here you will find all the material for our seminars. This repository will be updated every week, so say tuned (and git pull often)!

## Course content
Recommender systems are an integral part of our daily media consumption: they compile playlists on Spotify, suggest movies on Netflix, and select news content for personalized social media feeds on platforms like Facebook or Twitter. In the age of information overload, recommender systems provide orientation and assist users in making choices. Through data collection and statistical modeling, the underlying algorithms identify and present content that is considered most "relevant" to users. 

However, recommender systems are not objective observers or advisors; they carry specific norms and values that their creators consciously and unconsciously impart during the development and deployment of algorithms. These factors and their social impact are highly context-dependent. For example, recommender systems are often at the center of discussions about political polarization on digital platforms and have been associated with the reinforcement of "tunnel vision" among users by leading them into content funnels that may reduce exposure to diversity. 

This course centers on the question: how can recommender systems implement public values (e.g., trust, autonomy, diversity, sustainability)? To approach answers and develop prototypes, you are introduced to 
1. the concept of recommender systems and their connection to public values, 
2. value-sensitive design theory and methods (understanding the user, defining metrics, interface design), and 
3. the development of basic recommender systems for public media (e.g., content-based, collaborative-based, and hybrid filtering). 

This course approaches recommender systems from a humanities perspective; students are challenged to critically engage with data-driven technology with an explicit focus on values. It is less "hardcore" technical but decidedly interdisciplinary with a firm grounding in humanities/media studies. The course has three pillars: 
1. conceptual
2. design
3. technical

Within this integrative framework, you will explore the interplay between data, technology, and (public) values.

## Running the code

Students are expected to have basic Python skills. You are expected to have a working Python installation before the start of the course. We recommend you use Python 3.12.

### Creating a virtual environment
It is good practice to use a virtual environment to manage your installed Python libraries. See the [official Python documentation on working with virtual environments](https://docs.python.org/3/library/venv.html).

Install the Python libraries from the requirements file:

```sh
pip install -r requirements.txt
```

The course materials includes Jupyter notebooks (`.ipynb` files) and Python scripts (`.py` files). 

To work with the code, you are free to use a code editor or IDE you prefer. Visual Studio Code is a suitable program for the course. Their website includes extensive tutorials on [working with Python](https://code.visualstudio.com/docs/python/python-quick-start) and [working with Jupyter notebooks in Visual Studio Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).

You can also start Jupyter from a terminal using:

```sh
jupyter notebook
```

## Authors
This repository is maintained by [Erik Hekman](https://www.linkedin.com/in/erikhekman), [David Gauthier](https://www.uu.nl/staff/DGauthier), [Dennis Nguyen](https://www.linkedin.com/in/dennisnguyenphd/), [Jelte van Boheemen](https://www.uu.nl/medewerkers/JvanBoheemen), and [Luka van der Plas](https://www.uu.nl/medewerkers/LPvanderPlas).
