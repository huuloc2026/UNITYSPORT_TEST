def compress_json(data):
    # Lấy danh sách tất cả các khóa từ đối tượng đầu tiên trong data
    keys = list(data[0].keys())  # Lấy các tên trường (field names)
    
    # Khởi tạo một từ điển để lưu trữ các giá trị đã được tách ra
    compressed_data = {'keys': keys, 'data': []}
    
    # Duyệt qua các đối tượng trong danh sách và tách giá trị theo từng trường
    for entry in data:
        compressed_data['data'].extend(entry[key] for key in keys)
    
    return compressed_data

def read_json_file(file_path):
    # Đọc dữ liệu JSON từ file dưới dạng chuỗi
    with open(file_path, 'r') as file:
        return file.read()

def write_json_file(file_path, data):
    # Ghi dữ liệu JSON vào file dưới dạng chuỗi
    with open(file_path, 'w') as file:
        file.write(data)

def fix_json_null(json_str):
    # Thay thế 'null' thành 'None' để Python có thể hiểu
    return json_str.replace('null', 'None')

def convert_to_json_string(data):
    # Chuyển đổi dữ liệu thành chuỗi JSON (mô phỏng lại cấu trúc JSON)
    result_str = "{\n  \"keys\": ["
    
    # Dùng join thay vì vòng lặp để tối ưu hóa
    result_str += ",\n".join(f'  "{key}"' for key in data['keys'])
    result_str += "\n],\n  \"data\": ["
    
    result_str += ",\n".join(f'  "{entry}"' for entry in data['data'])
    result_str += "\n  ]\n}"

    return result_str

# Đọc dữ liệu từ file 'data.json' (dưới dạng chuỗi)
input_file = 'data.json'
output_file = 'minify-data.json'

# Đọc dữ liệu từ file
json_data_str = read_json_file(input_file)

# Sửa chuỗi JSON để thay thế 'null' thành 'None'
json_data_str = fix_json_null(json_data_str)

# Chuyển đổi từ chuỗi JSON thành danh sách Python (tự làm việc với chuỗi)
json_data = eval(json_data_str)  # Cẩn thận khi sử dụng eval với dữ liệu không tin cậy

# Kiểm tra nếu key tồn tại trong json_data
key = "select * from sport_events se where se.start_timestamp >= 1729875600 and se.start_timestamp <= 1729962000"
if key in json_data:
    # Nén dữ liệu nếu có khóa 'data'
    compressed_data = compress_json(json_data[key])

    # Chuyển dữ liệu nén thành chuỗi JSON thô
    compressed_json_str = convert_to_json_string(compressed_data)
    
    # Ghi dữ liệu đã nén vào file mới
    write_json_file(output_file, compressed_json_str)

    print(f'Data has been compressed and saved to {output_file}')
else:
    print("The specified key is missing in the input JSON.")
