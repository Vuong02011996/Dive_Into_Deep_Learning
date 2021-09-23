# Khái niệm
+ Định thức
+ Trị riêng và vector riêng
+ Độc lập tuyến tính.
+ Phụ thuộc tuyến tính.
+ Cơ sở(Basis).
+ Không gian sinh(Span).
+ Ma trận đơn vị.
+ Hạng của ma trân.
+ Ma trận ngịch đảo.
+ Chuẩn(Norm) của vector và ma trận.
+ Phép nhân ma trận.
+ Ma trận xác định dương.
+ Khử Gauss.

# Kí hiệu.
![](image/Bang%20ki%20hieu.png)

### 1. Chuyển vị(transpose) và Hermitian.
+ `Ma trận chuyển vị`: là ma trận được nhận từ ma trận cũ thông qua phép phản xạ gương qua đường chéo chính 
của ma trận ban đầu. (T).
+ `Ma trận A đối xứng` (symmetric matrix): nếu A chuyển vị = A.
+ `Chuyển vị liên hợp` (conjugate transpose): là chuyển vị ma trận có phần tử là số phức. (H- Hermitian)
+ Nếu chuyển vị liên hợp của một ma trận phức bằng chính nó thì ta nói ma trận đó Hermitian.

### 2. Phép nhân vô hướng.
#### Tích vô hướng của ma trận(??)
+ Ma trận **A**(m x n), **B**(n x p), **C = AB** => **C**(m x p)
  + <img src="image/Nhan%20hai%20ma%20tran.png" alt="drawing" width="500" height="100"/>
+ Để nhân được hai ma trận số hàng của ma trận thứ nhất phải bằng số cột của ma trận thứ hai.
+ Các tính chất của phép nhân ma trận :
  + Không có tính chất giao hoán: AB # BA.
  + Có tính chất kết hợp: ABC = (AB)C = A(BC)
  + Phân phối với phép cộng: A(B + C) = AB + AC
  + Chuyển vị của một tích bằng tích các chuyển vị theo thứ tự ngược lại.
  + <img src="image/Tich_chuyen_vi.png" alt="drawing" width="500" height="30"/>
#### Tích vô hướng của hai vector (Inner product).
+ Theo định nghĩa trên nếu coi vector là một trường hợp đặc biệt của ma trận. Tích vô hướng của hai vector **x, y**(n x 1):
+ <img src="image/Tich_vo_huong_vector.png" alt="drawing" width="500" height="100"/>
+ Nếu tích vô hướng của hai vector khác không bằng không. Hai vector đó vuông góc với nhau.
+ Ý nghĩa hình học Euclide:
+ <img src="image/hinh_hoc_tich_vo_huong.png" alt="drawing" width="500" height="30"/>

#### Tích vô hưởng của vector với ma trận.
+ Phép nhân của một ma trận A(m x n) với vector x(n x 1) là một vector b (m x 1) 
+ <img src="image/Nhan_vo_huong_ma_tran_vector.png" alt="drawing" width="500" height="100"/>
### 3. Phép nhân có hướng.
#### Nhân có hướng của ma trận (Hadamard hay element wise)
+ Tích Hadamard của hai ma trận cùng kích thước A, B (m x n) là ma trận C (m x n):
+ <img src="image/Hadamard.png" alt="drawing" width="500" height="30"/>

#### Nhân có hướng của hai vector 
+ [ref](https://apecceosummit2017.com.vn/tich-vo-huong-tich-co-huong/)
+ Tích có hướng của hai vector la một vector giả có phương vuông góc với mặt phẳng chứa hai vector đầu vào, chiều 
theo quy tắc bàn tay phải.
+ <img src="image/Nhan_co_huong_hai_vector.png" alt="drawing" width="500" height="100"/>



























