# **Catnip Cove Deployment &amp; Local Development**

![Am I Responsive mock-up of Catnip Cove](./documentation/features/responsive-screenshot.png)

**[Link to the Deployed Site]** - [Catnip Cove](https://catnip-cove-8a89db282e0c.herokuapp.com/)

## **Deployment Steps**
Catnip Cove is deployed on Heroku and uses AWS3 for staticfiles cloud storage.

**1. Install the project requirements by creating a Pipfile** <br/>
In the terminal, enter the command ```pip3 freeze > requirements.txt ``` and a file with all the requirements will be created.

**2. Create an external database on PostgreSQL.com** <br/>
The sqlite3 database that came with Django and which we have been using is only available for use in development. I needed to create a new database that is suitable for production.
* Go to [PostgreSQL.com](https://dbs.ci-dbs.net/)
* Enter your email address and click submit.
* An email will be sent to the above entered address with the database URL.

**3. Set up Heroku**
* Go to [Heroku.com](https://www.heroku.com/) and log in
* Choose the New button and from the dropdown, select *Create new app*
* Add your preferred app name and select your location and click the create app button
* Add the **DATABASE_URL** from the email you received above, to the Config Vars by going to the settings tab
* Click *Reveal Config Vars*
* Add a Config Var **DATABASE_URL** and paste your PostgreSQL database URL in as the value

**4. Connect the external database to GitPod**
* In your **env.py** file add a new key, **DATABASE_URL** and give it the value of the copied database URL <br/>
```bash
os.environ.setdefault("DATABASE_URL", "the_copied_database_url")
```
* Install the **dj-database-url** package version 0.5.0 and **psycopg2** in the terminal with **pip3** to allow us to parse the URL we have copied above to a format that Django can work with: <br/>
```bash
pip3 install dj_database_url==0.5.0 psycopg2
```
* and remember to add both to your **requirements.txt** file with: <br/>
```bash
pip3 freeze --local > requirements.txt
```
* At the top of the **settings.py** file, import **dj_database_url** underneath the import for os <br/>
```python
import os
import dj_database_url
```
* In the **settings.py** file, comment out the default database setting and replace it to use the **DATABASE_URL** environment variable <br/>
```python
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
```
* Run the showmigrations command in the terminal to confirm you are connected to the external database
```bash
python3 manage.py showmigrations
```
**Note:** this does not transfer the data, only the database structure
* If you are connected to the external database, you should see a list of migrations, but none of them are checked off
* Run the migrate command in the terminal
```bash
python3 manage.py migrate
```
**5. Fixtures**<br/>
**If you did not use fixtures to populate your database**, but instead manually added all your data via the Django admin, we now need to *transfer* the data from GitPod to your new database and we are going to do this using the **dumpdata** command. This will *dump* the data from SQLite into a JSON file (and later on the **loaddata** command to upload the JSON *dump* into the external database), both from the GitPod terminal.<br/>

**Dumpdata**
* First, we need to *dump* the data from SQLite into a JSON file. To do that we need to **make sure that GitPod is connected to SQLite.** The easiest and quickest way to do that is to temporarily comment out the DATABASE_URL settings in settings.py, and ﬁx the indentation:
```python
# if "DATABASE_URL" in os.environ:
#    DATABASES = {"default: dj_database_url.parse(os.environ.get("DATABASE_URL"))"}
# else:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
```
* Save the **settings.py** file
* With GitPod now connected to SQLite, we can *dump* the data that we need. The command syntax is:
```bash
python3 manage.py dumpdata app_name > filename.json
```
This will automatically create the JSON file and will dump all the model instances of the app into the file. Catnip Cove's **blog app** has Category, Post, and Comment models.
```bash
python3 manage.py dumpdata blog > blog.json
```
will dump all 3 models instances in the SQLite DB from the **blog app** into a file called blog.json.

You can run the same command again for the other apps. But bear in mind that the model/app that refers to another model in another app as Foreign Key needs to be uploaded after the one it refers to. For instance, the **donations app** refers to the *cat* model then you must load the **cats** first, otherwise, you'll get a fixture error.

**If you used fixtures for your project,** you can start to load in the fixtures here by **making sure that GitPod gets connected to our external Postgres database**
* In **settings.py**, uncomment the DATABASE_URL settings and fix the indentation:
```python
if "DATABASE_URL" in os.environ:
    DATABASES = {"default: dj_database_url.parse(os.environ.get("DATABASE_URL"))"}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
```
* Save the **settings.py** file
 GitPod is now connected to the external database. Run **migrate** just to make sure that the latest migrations are applied to this external db:
 ```bash
 python3 manage.py migrate
 ```
**Loaddata**
* Use **loaddata** to upload the products JSON file by running:
```bash
python3 manage.py loaddata cats.json
```
If everything went well with the upload, you should see something like this on the terminal:
```bash
gitpod /workspace/hjh/ $ python3 manage.py loaddata cats.json
Installed 130 object(s) from 1 fixtures
```
* Create a superuser for your new database
```bash
python3 manage.py createsuperuser
```
Follow the steps to create your superuser username and password.

**6. Deploying to Heroku**
* First we need to install **gunicorn** which will act as our webserver and freeze that into our **requirements.txt** file
```bash
pip3 install gunicorn
pip3 freeze > requirements.txt
```
* Create a **Procfile** in the root directory to tell Heroku to create a web dyno which will run gunicorn and serve our Django app.
```Procfile
web: gunicorn catnip_cove.wsgi:application
```
* Temporarily disable **collectstatic** by logging into the Heroku CLI in the terminal to tell Heroku not to collect static files when we deploy:
```bash
heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku-app-name
```
* We also need to add the hostname of our Heroku app to allowed hosts in **settings.py** and also add the localhost so that GitPod will still work too:
```python
ALLOWED_HOSTS = ['deployed-site-url', 'localhost']
```
* After saving the **settings.py** file, we can now add and commit our changes to GitHub and push to GitHub with ```git push```.
* Then using ```git push Heroku main``` to deploy to Heroku.

The app should be deployed, albeit without the static files as we are yet to set these up.

* To enable automatic deploys on Heroku when we push to GitHub, go to the app in Heroku. On the deploy tab, set it to connect to GitHub. Search for your repository and then click *connect*. Then click *Enable Automatic Deploys*.

**8. Generate SECRET_KEY**
1. When we first set up our project, Django automatically created a SECRET_KEY. Although you may not have committed this secret key to GitHub and have saved this instead on your **env.py** file and added this file to **.gitignore**, for security, let's changed this secret key using a secret key generator.
2. Go to [Djecrety Django Secret Key Generator](https://djecrety.ir/), click on the *Generate* button and copy the value.
3. Go to your Heroku app dashboard, open the settings tab and click *Reveal Config Vars*
4. Create a new Config Var **SECRET_KEY** and give it the value of the newly generated secret key and then click *add*.
5. Open your project's **settings.py** file and add:
```python
SECRET_KEY = os.environ.get('SECRET_KEY', '')
```
6. Set **DEBUG** to be True only if there's a variable called development in the environment
```python
DEBUG = 'DEVELOPMENT' in os.environ
```
Save the **settings.py** file, add, commit and then git push these changes.

**9. Set up Amazon Web Services' S3 to host our static files and images**
**Create an account** <br/>
* Create an AWS Account by going to [aws.amazon.com](https://aws.amazon.com/) and click on *create an aws account* by filling in your email and a password and choose a username for the account and select *continue*
* On the account type, select *personal*, fill out the required information, and click *create account and continue*
* Enter the credit card number which will be used for billing if the account goes above the free usage limits
* Complete the verification and once you confirm all the required information, your account will be created.
**Create a bucket**
* Once your signed in to your account, find S3 using the search bar, select and navigate to S3 to create a new bucket which will be used to store your static and media files
* Click the *create bucket* button and on the General configuration section, add the name of your bucket. It is a good idea to name the bucket the same as your project to keep your buckets organised and clear
* Select the region closest to you
* On the Object Ownership section, select *ACLs enabled* and then select *Bucket owner preferred*
* On the Block Public Access settings for this bucket section, uncheck *Block all public access*, check the *I acknowledge that the current settings might result in this bucket and the objects within becoming public* checkbox to make the bucket public and click *create bucket*
* Click the bucket you created and select the *properties* tab. Scroll down to find the *static web hosting* section and select *enable static web hosting*, tick *host a static website* and add *index.html* and *error.html* to the input fields for **Index document** and **Error document** respectively and click *save*.
* Open the permissions tab and copy the ARN (Amazon Resource Name). Navigate to the bucket policy section, click *edit* and select *policy generator*. From the *Select Type Policy* dropdown options, select S3 bucket policy. We want to allow all principal by adding the `*` to the input and the from the *Actions* dropdown, select *GetObject*.
* Paste the ARN we copied into the ARN (Amazon Resource Name) input field and click *add statement*, then click *generate policy*, copy the Policy from the new popup and paste it into the bucket policy editor and add `/*` at the end of the resource value to allow access to all resources in this policy and finally, click *save*.
* AWS has changed the format of their **cross-origin resource sharing (CORS)** configuration so we need to paste the update code below to the CORS section:
```json
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
* For the **Access control list (ACL)** section, click *edit* and tick *List* for **Everyone (public access)** and accept the warning box. If the edit button is disabled you need to change the **Object Ownership** section above to **ACLs enabled**.

**Create Group, Policies and Users using AWS's Identity and Access Management (IAM) service**<br/>
* Find IAM using the search bar, select and navigate to IAM to create a group, create an access policy to give the group access to the S3 bucket and assign the user to the group so it can use the policy to access the files.
* Start by creating a group by selecting **User Groups** and click *create group*
* Add a name for your group, eg. manage-catnip-cove, then click *create user group* button
* Click on the user group you just created and then click on permissions
* Click the Add Permissions button and select attach policies from the dropdown
* Search for S3 and select the pre-built *AmazonS3FullAccess* policy and click *attach policies*
* Then you need to create a user for the group. Click *Users* from the left sidebar and then click the *add users* button and add a name for the user, eg. catnip-cove-staticfiles-user
* Next make sure *programmatic access* is selected from Access Type and click *next: permissions*
* Add user to the group and click *next: tags*, *next: review* and then the *create user* button.
* Next you need to download the .csv file which will contain this user's access key and secret access key which we'll use to authenticate them from our Django app.
* Click on the user name link and select the *security credentials* tab.
* Scroll to the *Access Keys* section and click on *Create access key* button
* Select 'Application running outside AWS', and click next
* On the next screen, you can leave the 'Description tag value' blank. Click 'Create Access Key'
* Click the 'Download .csv file' button; This will trigger a download of the details into a spreadsheet - store this somewhere safe.

**10. Connecting Django to S3**
* Install two new packages: **boto3** and **django-storages**
```bash
pip3 install boto3
pip3 install django-storages
pip3 freeze > requirements.txt
```
* Add `storages` to the installed apps in **settings.py**
* Also on **settings.py**, add the bucket configuration:
```python
    if 'USE_AWS' in os.environ:
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=9460800',
        }

        AWS_STORAGE_BUCKET_NAME = 'your bucket name goes here'
        AWS_S3_REGION_NAME = 'your selected region goes here'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```
* Open the .csv file we downloaded earlier and go to Heroku app dashboard and add these to Config Vars:
| Key | Value |
| :-- | :-- |
| AWS_ACCESS_KEY_ID | The access key value from the .csv file |
| AWS_SECRET_ACCESS_KEY | The secret access key value from the .csv file |
| USE_AWS | True |
* Remove **COLLECTSTATIC** variable from the Config Vars
* Create **custom_storages.py** file and add:
```python
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
* Next, go back to **settings.py** file and tell it that for static file storage, we want to use our storage class we just created and that the location it should save static files us a folder called static. And then do the same thing for media files using the default file storage and media files location settings.
```python
    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
```
* We also need to override and explicitly set the URLs for static and media files using our custom domain and the new locations:
```python
    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
* Next, save the **settings.py** file, add all these changes, commit them and then issue a git push which will trigger an automatic deployment to Heroku. With that done if we look at the build log. We can see that all the static files were collected successfully
* To handle the media files, Let's go to s3 and create a new folder called media then click *upload*. Add the product images files, click *next* and under manage public permissions, select *grant public read access to these objects.* Then click *next* through to the end and finally, click *upload*.

11. Setting up Stripe
* Log in to Stripe, click the *developers* link, and then *API Keys*
* Add them as Config Vars in Heroku
* Now we need to create a new webhook endpoint since the current one is sending webhooks to our gitpod workspace. We can do that by going to webhooks in the developer's menu and clicking *add endpoint*.
* Add the URL for our Heroku app, followed by /donations/WH and select *receive all events and add endpoint*.
* We can now reveal our webhooks signing secret and add that to our Heroku config variables.

---
## How to Fork the repository
To create a copy of the repository on your account and change it without affection the original project, click the *Fork* button on GitHub:
* On the Catnip Cove repository, click the *Fork* button on the top right side of the page.
* A forked version of Catnip Cove will be available as one of your repositories on GitHub

---
## How to Clone the repository
* On the Catnip Cove repository page, click the *<> Code* button (left of the green *GitPod* button)
* Choose from *HTTPS, SSH and GitHub CLI* (I recommend *HTTPS*) and *copy the link* given
* On your IDE, open *Git Bash*
* Enter the command `git clone` followed by the copied link
* Set up a virtual environment if not using the Code Institute template
* To install the packages from the requirements.txt file
```bash
pip3 install -r requirements.txt
```