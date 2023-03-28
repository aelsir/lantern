# Django Blog App

This is a simple blog app built using Django for Lantern Company. It contains a basic two views: post_list and post_detail.

## Installation

To install this app, follow these steps:

1. Clone the repository: git clone <https://github.com/aelsir/lantern.git>
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`

## Structure

### lantern

**lantern** is the main django project and it contain the settings and global configurations.

### core

**core** is the main app in the project and you can refer to the `urls.py` file inside the core app to start mapping the routes of the application.

## Models

The main model of the app is **Post** model it contain all of the data related to the post, and link to the autor aka **User**.

## Usage

### Branches
I was experimenting with different frontend libraries and rewrote the entire blog in both `bootstrap` and `tailwind` and deployed them in different branches
1. `master` contain the main branch that is been deployed and currently it's build on bootstrap
2. `bootstap` contain the blog styled using bootstrap library.
3. `tailwind` contain the blog styled using tailwind library, also if you want to use it will need more configurations including: `installing nodejs modules` and `running tailwind engine`.


### post_list

This view displays a list of all the posts that have been published on the blog. To access this view, go to <http://localhost:8000/>. Each post is displayed as a clickable link that will take you to the post_detail view.

![Posts List](https://lh3.googleusercontent.com/VEExaWzIozInfxoam2etTb3xQgOfT23ANZHxKX7u_7Gn6KEza3rYl-DFjw_tgtf0rW7DKB1ZxyG-ZeV-7mYgyk4w0UBuWYbCHODEY-qMH8FwL95rdLKJfhK-I9otX3prI9crcjfh7Go=w2400)

### post_detail

This view displays the details of a single post. To access this view, click on the link for the post you want to view in the post_list view. The details that are displayed include:

- Title: The title of the post.
- Author: The name of the writer who published the post.
- Published Time: The time when the post was published.
- Body: The full body of the post.

![Post Detail](https://lh3.googleusercontent.com/N281i0kHJFoXonS9pdrmY4BSBDgRoK8OW4UWkE_9TEEOUAR37thvfmU-6XpYQdITudVvvuwPfG62MoFki2VHE-vZtMWlwlLCwIPGYD4YZ9pFhXZnfzX74w8AZH5UHkKJnfMVRKBv60c=w2400)

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: git checkout -b my-new-feature
3. Make your changes and write tests to ensure that they work correctly.
4. Submit a pull request to the master branch.

## License

This project is licensed under the MIT License.

## Contact

you can contact and follow me here on GitHub or social media at:

- [LinkedIn](https://www.linkedin.com/in/aelsir/)
- [Facebook](https://www.facebook.com/ahmed.elsir.khalfalla/)
