# WysaAPITesting
The following are the steps to set up and test the api endpoint.
1. Install the request package and other packages such as jsonschema and pytest(if required) using `pip install requests jsonschema pytest` command
2. Now, you need to define the structure of the data you expect to receive from the API. This could be in the form of a JSON schema or a simple dictionary structure, this is why we installed the jsonschema package.
3. write a script to send a request to the API endpoint you want to test, basically make the GET call to the endpoint.
4. Compare the response you received from the API with the expected structure. This can be done manually or through automated testing using a testing framework such as pytest.
5. Using the try except check or validate if the response you have received is same as expected or not
6. If you need to check specific values or conditions within the response, you can add additional assertions as well on this.
7. We can further automate this process, as in we can integrate this validation into a CI/CD pipeline or automated testing framework to ensure that API responses continue to meet expectations as the API evolves.
8. To run the python file we can use the command `python filename.py` or `pytest filename.py`
