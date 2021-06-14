import json

class JsonValidator():

    def __init__(self):
        self.invalid_records = set()
        self.processed_duplicate = {}

    def remove(self, record):
        data = {}
        for k in record.keys():
            if k != "id":
                data[k] = record[k]
        return data

    def is_processed(self, record):
        if str( self.remove(record) ) in self.processed_duplicate:
            return True

        self.processed_duplicate[str( self.remove(record) )] = record['id']
        return False

    def null_check(self, record, key):
        if key not in record.keys() or record[key] is None or len(record[key]) == 0:
            return True

        return False

    def validate_zip_code(self, zip_code):
        if zip_code.isnumeric() and ( len(zip_code) == 5 or len(zip_code) == 9):
            return True
        if '-' in zip_code:
            a = zip_code.split('-')
            if len(zip_code.split('-')) == 2:
                if zip_code.split('-')[0].isnumeric() \
                and len(zip_code.split('-')[0]) == 5 \
                and zip_code.split('-')[1].isnumeric() \
                and len(zip_code.split('-')[1]) == 4:
                    return True
        return False

    def is_valid(self, record):
        if self.null_check(record, 'name') \
            or self.null_check(record, 'address') \
            or self.null_check(record, 'zip') \
            or not self.validate_zip_code(record['zip']):
            return False
        return True

    def validate_file(self, path):
        with open(path) as file:
            data = json.load(file)
            for d in data:
                if self.is_processed(d):
                    self.invalid_records.add(d['id'])
                    if str( self.remove(d) ) in self.processed_duplicate:
                        self.invalid_records.add( self.processed_duplicate[str( self.remove(d) )] )
                elif not self.is_valid(d):
                    self.invalid_records.add(d['id'])
        return self.invalid_records
        # print(len(self.invalid_records))

if __name__ == "__main__":
    validator = JsonValidator()
    invalid_ids = validator.validate_file("data.json")
    for id in invalid_ids:
        print(id)
