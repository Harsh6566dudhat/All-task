sample_dict = {
    "name": "Harsh",
    "age": 25,
    "salary": 80000,
    "city": "New york"
}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)
