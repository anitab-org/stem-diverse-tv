# STEM Diverse TV

[![project chat](https://img.shields.io/badge/zulip-join_chat-brightgreen.svg)](https://anitab-org.zulipchat.com/#narrow/stream/225705-STEM-diverse-tv)

# stem-diverse-tv

STEM Diverse TV is a project which gather and provide inspiring, motivating, informative, educational and supportive videos about diversity in STEM. This is the backend of the project.

**Table of Contents**

- [Setup and run](#setup-and-run)
- [Contributing](#contributing)
- [Contact](#contact)
- [License](#license)

## Setup and run

To setup the project locally follow the instructions:

Please make a virtual environment and run the following commands.
```
virtualenv venv --python=python3
source ./venv/bin/activate
pip3 install -r requirements.txt 
```

- Please download Firebase Admin SDK service json file from Firebase Console, You can download the file by following below steps:
    1.  Go to `Project Settings/Service accounts`
    2.  Click on `Generate New Primary Key`
    3.  Place the file in project's root directory and rename it to `google-credentials.json`
- Make .env file from given .env.template file and add details like API_KEY, which is a web api key from firebase. Find your project's web api key in project's overview tab on firebase console.

After this, execute:
```
python run.py
```
or
```
python3 run.py
```

#### Fork

_**Note**_: *This is only needed if you want to contribute to the project.*

If you want to contribute to the project you will have to create your own copy of the project on GitHub. You can do this by clicking the Fork button that can be found on the top right corner of the [landing page](https://github.com/anitab-org/stem-diverse-tv) of the repository.

#### Clone

_**Note**_: *For this you need to install git on your machine. You can download the git tool from [here](https://git-scm.com/downloads).*

 * If you have forked the project, run the following command -

   `git clone https://github.com/YOUR_GITHUB_USER_NAME/stem-diverse-tv`

   where `YOUR_GITHUB_USER_NAME` is your GitHub handle.

 * If you haven't forked the project, run the following command -

   `git clone https://github.com/anitab-org/stem-diverse-tv`

 * Now after you cloned the repository, get into the anitab-org.github.io directory by -

   `cd stem-diverse-tv`

#### Remote

_**Note**_: *This is only needed if you want to contribute to the project.*

When a repository is cloned, it has a default remote named `origin` that points to your fork on GitHub, not the original repository it was forked from. To keep track of the original repository, you should add another remote named upstream. For this project it can be done by running the following command -

`git remote add upstream https://github.com/anitab-org/stem-diverse-tv`

You can check that the previous command worked by running `git remote -v`. You should see the following output:

```
$ git remote -v
origin  https://github.com/YOUR_GITHUB_USER_NAME/stem-diverse-tv (fetch)
origin  https://github.com/YOUR_GITHUB_USER_NAME/stem-diverse-tv (push)
upstream        https://github.com/anitab-org/stem-diverse-tv (fetch)
upstream        https://github.com/anitab-org/stem-diverse-tv (push)
```

## Contributing

**This project is under active development**

Please read our [Contributing Guidelines](docs/contributing_guidelines.md), [Code of Conduct](docs/code_of_conduct.md) and [Reporting Guidelines](docs/reporting_guidelines.md) thoroughly.


## Contact

If you have any questions or want to discuss something about this repo, feel free to reach out to our team on our Zulip channel [#Design-team](https://anitab-org.zulipchat.com/#narrow/stream/216323-design/topic/STEM.20Diverse.20TV). If you are a new contributor, head over to this project's stream (https://anitab-org.zulipchat.com/#narrow/stream/225705-STEM-diverse-tv) on Zulip to see ongoing discussions.

## License

The project is licensed under the GNU General Public License v3.0. Learn more about it in the [LICENSE](LICENSE) file.
