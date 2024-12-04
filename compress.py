def compress_json(data):
    # Lấy danh sách tất cả các khóa từ đối tượng đầu tiên trong data
    keys = list(data[0].keys())  # Lấy các tên trường (field names)
    
    # Khởi tạo một từ điển để lưu trữ các giá trị đã được tách ra
    compressed_data = {'keys': keys, 'data': []}
    
    # Duyệt qua các đối tượng trong danh sách và tách giá trị theo từng trường
    for entry in data:
        # Chuyển các giá trị thành chuỗi và nối lại chúng bằng dấu phẩy
        compressed_data['data'].append(
            f"\"{', '.join([str(entry[key]) for key in keys])}\""
        )
    
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
    
    # Chuyển đổi dữ liệu 'data' thành chuỗi, mỗi phần tử là một chuỗi giá trị
    result_str += ",\n".join(
        entry for entry in data['data']
    )
    result_str += "\n  ]\n}"

    return result_str

def reverse_json_null(json_str):
    # Thay thế 'None' thành 'null' để trả lại dữ liệu JSON đúng định dạng
    return json_str.replace('None', 'null')

# Đọc dữ liệu từ file 'data.json' (dưới dạng chuỗi)
input_file = 'data.json'
output_file = 'minify-data.json'

# Đọc dữ liệu từ file
json_data_str = read_json_file(input_file)

# Sửa chuỗi JSON để thay thế 'null' thành 'None'
json_data_str = fix_json_null(json_data_str)

# Chuyển đổi từ chuỗi JSON thành danh sách Python (cẩn thận với eval)
try:
    # Chuyển chuỗi JSON thành đối tượng Python, cẩn thận với eval
    json_data = eval(json_data_str)  # Cẩn thận khi sử dụng eval với dữ liệu không tin cậy
except Exception as e:
    print(f"Error while evaluating JSON string: {e}")
    exit()

# Kiểm tra nếu key tồn tại trong json_data
key = "select * from sport_events se where se.start_timestamp >= 1729875600 and se.start_timestamp <= 1729962000"
if key in json_data:
    # Nén dữ liệu nếu có khóa 'data'
    compressed_data = compress_json(json_data[key])

    # Chuyển dữ liệu nén thành chuỗi JSON thô
    compressed_json_str = convert_to_json_string(compressed_data)
    
    # Chuyển null về lại thành 'None' để Python hiểu và sau đó chuyển ngược lại khi xuất ra
    compressed_json_str2 = reverse_json_null(compressed_json_str)
    
    # Ghi dữ liệu đã nén vào file mới
    write_json_file(output_file, compressed_json_str2)
    
    print(f'Data has been compressed and saved to {output_file}')
else:
    print("The specified key is missing in the input JSON.")


