#UFC Official Shop


Creating this README.MD which will guide you to run the UFC Shop Application on AWS environment.


unzip the repository and perform below steps to get this application working.

create virtual environment by 
    python -m venv env
Activate the virtual envirmnoment
    source env/bin/activate
go to repositoy
    cd ufcdublin
    cd UFCdublinshop
run below commands,
    pip install -r requirements.txt

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver 8080

Access the url and check all the functionalities.

To deploy the application to the production environment like elastic beanstalk.

1. Through command line,

    go to AWS console and create an environment using cloud9 IDE, keep all the details default.

    follow all the above steps to run the application.
    then deactivate the virtual environment by
        deactivate
    
    install elastic beanstalk cli
        python -m pip install --upgrade pip
    
    check the elastic beanstalk version
        eb --version

    create an application
        eb init -r us-east-1 -p python-3.7 <applicationName>
        
        eb init

        check Y to use codecommit repository
        provide Name of the repository and branch as main

        click Y for SSH setup
        keep passphrase blank

    create an elastic beanstalk environment
        eb create <envName>

    It will take 3-4 minutes to create an environment.
    
    Go to codecommit service, and under clone URL,
    copy HTTP(GRC) URL

    go to project directory in terminal and,
        git clone <codecommitCopiedURL>

    remote origin will be assigned to codecommit.
        git add .
        git commit -m "Initial Commit"
        git push

    it will push all the changes to CodeCommit

    Now deploy the application,
        eb deploy

    After successful deployment,
        eb open

    The website will be accessible on a production environment that is on elastic beanstalk.

2. Through CodePipeline

    Go to AWS Elastic Beanstalk console,

    create environment,
    provide the application name and environment name
    provide the platform as python and version as python-3.7 and create the environment

    after successful creation of the environment,
    go to AWS CodePipeline service,
    provide the name of the pipeline and keep all the below details same,
    In the next step keep the source code provider as CodeCommit.

    then skip the BUILD stage,
    in the next stage,
    chose Elastic Beanstalk as a Deploy provider and provide the application name and environment that we created just before.

    The pipeline will be created and after successful stages, access the website from elastic beanstalk console.
    Link of the Deployed application:
    http://goa-env.eba-2ccms9gs.us-east-1.elasticbeanstalk.com/store
    http://ufcnate.us-east-1.elasticbeanstalk.com/store

    Private Repo Gitlink- https://github.com/aakashpatil22/UFCdublinshop.git
