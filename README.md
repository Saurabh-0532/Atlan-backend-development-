# Google Forms CLONE


<details>
<summary>
More screenshots
</summary>

![Google Forms clone demo](https://drive.google.com/uc?export=view&id=1QhPVWHXKApcv5V6FzrHRzut7a5-1Mgp4)
![Google Forms clone demo](https://drive.google.com/uc?export=view&id=1Nwz642ORdTCd6KdsaN28Tt142K3wH-pt)
##### For the best experience, please use a device with a width of at least 350p
</details>
## Built using:
- Python with Django framework and Jinja templating language
- Vanilla Javascript

## Getting started:
- Clone this repository or fork it
    - To clone this repository type git clone `https://github.com/Saurabh-0532/Atlanbackend` on your command line
    - To fork this repository, click fork button of this repository then type git clone `https://github.com/<your username>/google-form-clone.git`
- Install all the dependencies of this project by typing `pip install -r requirements.txt`
- Migrate the database by typing `python manage.py migrate` on the command line
- Run the project locally by typing `python manage.py runserver` on the command line
    - NB: to run it on your local network, type `python manage.py runserver 0.0.0.0:8000`
- You project will be accessible in your localhost or local network.

## Deployment
For deployment open the pdf 'design specification' in the folder name 'Documents' 
## Note 
1. For running Google sheet API uncomment the code from line 18 to line 23 under  and line 499 inside the "def view_form(request, code)" in ../index/views
2. For running SMS API un comment the line 562 inside the "def submit_form(request, code)" function in ../index/views
3. Both API will work only if you set up the credential in setting fils i.e. ../form/settings folder from line 140 to line 146

## License
