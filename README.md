# Django Blog App

This is a simple blog app built using Django for Lantern Company. It contains a basic two views: post_list and post_detail.

## Installation

To install this app, follow these steps:

1. Clone the repository: git clone <https://github.com/aelsir/lantern.git>
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`

## Usage

### post_list

This view displays a list of all the posts that have been published on the blog. To access this view, go to <http://localhost:8000/>. Each post is displayed as a clickable link that will take you to the post_detail view.

### post_detail

This view displays the details of a single post. To access this view, click on the link for the post you want to view in the post_list view. The details that are displayed include:

- Title: The title of the post.
- Author: The name of the writer who published the post.
- Published Time: The time when the post was published.
- Body: The full body of the post.

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
