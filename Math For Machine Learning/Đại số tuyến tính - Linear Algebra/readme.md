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
**1. Tích vô hướng của ma trận(??)**
+ Ma trận **A**(m x n), **B**(n x p), **C = AB** => **C**(m x p)
  + <img src="image/Nhan%20hai%20ma%20tran.png" alt="drawing" width="500" height="100"/>
+ Để nhân được hai ma trận số hàng của ma trận thứ nhất phải bằng số cột của ma trận thứ hai.
+ Các tính chất của phép nhân ma trận :
  + Không có tính chất giao hoán: AB # BA.
  + Có tính chất kết hợp: ABC = (AB)C = A(BC)
  + Phân phối với phép cộng: A(B + C) = AB + AC
  + Chuyển vị của một tích bằng tích các chuyển vị theo thứ tự ngược lại.
  + <img src="image/Tich_chuyen_vi.png" alt="drawing" width="500" height="30"/>
**2. Tích vô hướng của hai vector (Inner product).**
+ Theo định nghĩa trên nếu coi vector là một trường hợp đặc biệt của ma trận. Tích vô hướng của hai vector **x, y**(n x 1):
+ <img src="image/Tich_vo_huong_vector.png" alt="drawing" width="500" height="100"/>
+ Nếu tích vô hướng của hai vector khác không bằng không. Hai vector đó vuông góc với nhau.
+ Ý nghĩa hình học Euclide:
+ <img src="image/hinh_hoc_tich_vo_huong.png" alt="drawing" width="200" height="30"/>

**3. Tích vô hưởng của vector với ma trận.**
+ Phép nhân của một ma trận A(m x n) với vector x(n x 1) là một vector b (m x 1) 
+ <img src="image/Nhan_vo_huong_ma_tran_vector.png" alt="drawing" width="500" height="100"/>
### 3. Phép nhân có hướng.
**1. Nhân có hướng của ma trận (Hadamard hay element wise)**
+ Tích Hadamard của hai ma trận cùng kích thước A, B (m x n) là ma trận C (m x n):
+ <img src="image/Hadamard.png" alt="drawing" width="200" height="30"/>

**2. Nhân có hướng của hai vector** 
+ [ref](https://apecceosummit2017.com.vn/tich-vo-huong-tich-co-huong/)
+ Tích có hướng của hai vector la một vector giả có phương vuông góc với mặt phẳng chứa hai vector đầu vào, chiều 
theo quy tắc bàn tay phải.
+ <img src="image/Nhan_co_huong_hai_vector.png" alt="drawing" width="500" height="100"/>

### 4. Ma trận đơn vị(identity matrix) và ma trận nghịch đảo(inverse matrix).
**1. Ma trận đơn vị.**
   + `Đường chéo chính ` của một ma trận là tập hợp các điểm có chỉ số hàng và cột như nhau.
   + Một ma trận đơn vị bậc nlà một ma trận đặc biệt trong R (n x n) với các phần tử trên đường chéo chính bằng 1, 
   các phần tử còn lại bằng 0. (I - identity matrix )
   + Ma trận đơn vị I(n x n) bậc n có tính chất đặc biệt trong phép nhân:
     + A (m x n): AI = A.
     + B (n x m): IB = B.
     + **x**(n x 1): Ix = x.
   
**2. Ma trận nghịch đảo.**
   + Ma trận vuông A (n x n) là `khả nghịch(invertible, nonsingular hoặc nondegenerate)` nếu tồn tại ma trận vuông B (n x n) 
   sao cho AB = I. Ma trận B được gọi là ma trận nghịch đảo của A.
   + Nếu A khả nghịch thì ma trận nghịch đảo (B) thường kí hiệu là: A<sup>-1</sup>
   + Ý nghĩa:
   + <img src="image/ma_tran_nghich_dao.png" alt="drawing" width="500" height="300"/>
   + Giả sử ma trận A, B khả nghịch thì tích của chúng cũng khả nghịch: (AB)<sup>-1</sup> = B<sup>-1</sup>A<sup>-1</sup>. Giống 
    với tính chất chuyển vị của tích ma trận.
   
**3. Một số ma trận khác.**
+ Ma trận đường chéo (diagonal matrix )
+ Ma trận tam giác trên (upper triangular matrix )
+ Ma trận tam giác dưới (lower triangular matrix )
    



























