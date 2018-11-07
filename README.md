# Arkham_bot

! This project is nearly completed but is as of yet, incomplete. The current trained model relies on restoring the training session with the saved checkpoints and arguments. This however does not work the same way when loading from S3 to Lambda because Tensorflow's restore_session function expects a file directory and does not accept an S3 file object.

Objective:

Tensorflow: Train a model on the collected works of H.P. Lovecraft in order to generate variable lengths of 'Lovecraft-like' text.

S3 & Lambda: Host the trained model in S3 and load it as needed from the Flask application script in Lambda. This is expected to execute when the application recieves the appropriate POST reqeust.

Twitter: Use the web hook API and respond to mentions with 'Lovecraft-like' text. This allows the app to be reactive instead of running uneccesarily.
