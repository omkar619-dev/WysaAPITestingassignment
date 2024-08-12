The following are the steps to set up and test the api endpoint.

Install the request package and other packages such as jsonschema and pytest(if required) using pip install requests jsonschema pytest command
Now, you need to define the structure of the data you expect to receive from the API. This could be in the form of a JSON schema or a simple dictionary structure, this is why we installed the jsonschema package.
write a script to send a request to the API endpoint you want to test, basically make the GET call to the endpoint.
Compare the response you received from the API with the expected structure. This can be done manually or through automated testing using a testing framework such as pytest.
Using the try except check or validate if the response you have received is same as expected or not
If you need to check specific values or conditions within the response, you can add additional assertions as well on this.
We can further automate this process, as in we can integrate this validation into a CI/CD pipeline or automated testing framework to ensure that API responses continue to meet expectations as the API evolves.
To run the python file we can use the command python filename.py or pytest filename.py