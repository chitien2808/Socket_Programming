# Remote Control Application - Môn học Mạng máy tính
## Thông tin nhóm
| MSSV | Họ và tên | Vai trò |
|----------|----------|----------|
| XXXXX | Nguyễn Ngọc Thanh Hằng | Nhóm trưởng |
| Row2Col1 | Row2Col2 | Row2Col3 |
| Row3Col1 | Row3Col2 | Row3Col3 |


## Thông tin đồ án
### Tổng quan
Đồ án lập trình ứng dụng sử dụng socket và ngôn ngữ Python để tạo một kết nối qua mạng giữa client và server. 
Thông qua giao diện người dùng đơn giản, người dùng có thể truy cập và điều khiển các tính năng của máy chủ từ xa.
### Tính năng chính
1. Xem Process
2. Xem Running Application
3. Chụp ảnh màn hình
4. Bắt phím (keystroke)
5. Shutdown
## Chi tiết về các tính năng
### Xem process
Phía server ta sử dụng thư viện [psutil](https://pypi.org/project/psutil/) để có thể tương tác được các process đang chạy,
sau khi nhận được tín hiệu từ client gửi lên server sẽ lấy thông tin các process và gửi về dưới dạng chuỗi cho phía client.
| Tên Hàm                     | Mô Tả                                                          | Vị Trí   |
|-----------------------------|----------------------------------------------------------------|----------|
| `receiveProcess`            | Nhận và ghi thông tin process vào một tệp.                   | Client   |
| `receiveStatus`             | Nhận trạng thái (kill thành công hay không)            | Client   |
| `killProcess`               | Kill process dựa trên PID của nó.            | Server   |
| `listProcess`               | Lấy thông tin tất cả process và gửi cho client.                | Server   |
### Xem Running Application
Để xác định các process nào là "Application" ta sẽ in ra các process đang được hiện ở thanh taskbar của Windows. Để làm viêc đó ta sử dụng 
thư viện [pywinauto](https://pywinauto.readthedocs.io/en/latest/). Tính năng tắt ứng dụng ta sẽ sử dụng thư viện mặc định [os](https://docs.python.org/3/library/os.html) của python. Ngoài ra thư viện [AppOpener](https://pypi.org/project/appopener/) hỗ trợ ta mở các ứng dụng một cách dễ dàng
| Tên Hàm                  | Mô Tả                                                               | Vị Trí  |
|--------------------------|---------------------------------------------------------------------|---------|
| `receiveRunningApp`      | Nhận danh sách ứng dụng đang chạy và ghi vào tệp.                   | Client  |
| `receiveStatus`          | Nhận trạng thái (kill/open - ok/err).    | Client  |
| `openApp`                | Mở ứng dụng và gửi trạng thái (thành công hay không)               | Server  |
| `killRunningApp`         | Tắt ứng dụng đang chạy dựa trên PID và gửi phản hồi.               | Server  |
| `listRunningApp`         | Lấy danh sách tất cả các ứng dụng đang chạy và gửi cho client.          | Server  |

### Chụp ảnh màn hình
Module ImageGrab của thư viện [Pillow](https://pypi.org/project/Pillow/) dễ dàng hỗ trợ ta chụp ảnh màn hình của máy server sau khi nhận tín hiệu từ phía client. Nhiệm vụ còn lại là gửi các bit ảnh về thông qua socket.
| Tên Hàm             | Mô Tả                                                                                   | Vị Trí  |
|---------------------|-----------------------------------------------------------------------------------------|---------|
| `saveImage`         | Mở file dialog để lưu ảnh                                                               | Client  |
| `readImage`         | Đọc hình ảnh từ socket, lưu trữ nó và thông báo rằng hình ảnh đã được nhận thành công.  | Client  |
| `sendScreenShot`    | Chụp ảnh màn hình, chuyển nó thành dữ liệu byte và gửi nó qua socket.                   | Server  |
### Bắt phím (Keystroke)

Tính năng Keystroke được thiết kế để ghi lại tất cả các sự kiện liên quan đến bàn phím trên server và sau đó truyền chúng đến client. Khi người dùng bấm phím "hook" hàm hook sẽ bắt đầu quá trình bắt phím trên máy chủ (quá trình này sẽ được thực hiện trên một thread riêng để luôn giữ kết nối giữa server và client). Các module hỗ trợ bắt phím được cung cấp trong thư viện [pynput](https://pypi.org/project/pynput/).
| Tên Hàm                | Mô Tả                                                                                                      | Vị Trí  |
|------------------------|-----------------------------------------------------------------------------------------------------------|---------|
| `receiveKeylogger`     | Nhận dữ liệu keylogger từ máy chủ, lưu nó và thông báo rằng dữ liệu đã được nhận thành công.             | Client  |
| `on_key_press`         | Ghi lại mỗi phím được nhấn và lưu chúng vào một tệp.                                                       | Server  |
| `hook`                 | Khởi tạo một người nghe (listener) để ghi lại mỗi phím được nhấn.                                         | Server  |
| `deleteKeyLoggerFile`  | Xóa nội dung của tệp keylogger.                                                                           | Server  |
| `sendKeyLogger`        | Đọc dữ liệu từ tệp keylogger, xóa nó và sau đó gửi nội dung đó đến máy khách.                             | Server  |
| `startedKeyLogger`     | Khởi động quá trình keylogging bằng cách thiết lập một hook và khởi tạo một thread mới để ghi lại phím.  | Server  |


