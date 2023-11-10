# Ensure you have Python set up on your machine to run this application

# To Run the Application, first activate the virtual environment:

    source .env/bin/activate

# You may also have to install some requirements to ensure this works:

    pip install -r requirements.txt

# To run it, you can use the following command:

    python main.py

# To run unit tests, run the following command:

    python -m unittest -b

During running of the application, you will be asked to enter a series of inputs, to determine the Department, Category, Sub Category and Type you wish to calculate and query fees upon.

You will be able to simply type the number associated to the selection to simplify the querying process.

As of the current implementation, please note that selecting 'All' anytime during the input selection process will automatically take you to confirmation and query all the subsequent children and sub-children of that specific node in the tree. This was done intentionally to avoid exponentinally complicating the querying procedure. I would look into being able to granularly refine the querying parameters as a future improvement but for now, I've designed this as such to be stratightforward and intuitive to use as much as possible.

Feel free to ignore the TODO comments littered throughout the application. These are notes for myself to dwell upon and investigate further for my own personal education
