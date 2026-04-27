# Tính số cách chọn các đối tượng

<!-- chunk:0 level:0 source:https://toanmath.com/2020/03/tinh-so-cach-chon-cac-doi-tuong.html -->
Bài viết hướng dẫn phương pháp giải dạng toán tính số cách chọn các đối tượng, thường gặp trong chương trình Đại số và Giải tích 11: Tổ hợp và xác suất.

1. PHƯƠNG PHÁP GIẢI TOÁN
+ Xác định tập hợp chứa các đối tượng cần chọn.

+ Xác định số đối tượng cần chọn.

+ Xác định quy cách chọn.

+ Dùng công thức tổ hợp tìm số cách chọn theo quy cách đó.

Lưu ý: Việc xác định quy cách chọn các đối tượng là rất quan trọng, chẳng hạn nếu chọn $k$ đối tượng trong $n$ đối tượng theo quy cách chọn lần lượt từng đối tượng khác với theo quy cách chọn một lần $k$ đối tượng.

## Bài tập

## Bài 1: Một tổ học sinh có $10$ người gồm $6$ nam và $4$ nữ. Hỏi có bao nhiêu cách chọn ra nhóm $5$ người để làm trực nhật mà nhóm đó không có quá $1$ nữ.

Lời giải:

+ Trường hợp 1: Chọn $4$ học sinh nam và $1$ học sinh nữ có: $C_6^4C_4^1 = 60$ cách chọn.

+ Trường hợp 2: Chọn $5$ học sinh nam có: $C_6^5 = 6$ cách chọn.

Vậy tất cả có $60 + 6 = 66$ cách chọn $5$ người trong đó có không quá $1$ nữ.

## Bài 2: Một lớp có $10$ học sinh nam và $10$ học sinh nữ. Cần chọn ra $5$ học sinh để đi làm công tác “Mùa hè xanh”. Hỏi có bao nhiêu cách chọn nếu trong $5$ học sinh đó phải có ít nhất:

## Bài tập 1. Hai học sinh nữ và hai học sinh nam.

## Bài tập 2. Một học sinh nữ và một học sinh nam.

Lời giải:

1) Có hai khả năng xảy ra:

Chọn được $2$ nữ và $3$ học sinh nam có: $C_{10}^2C_{10}^3 = 5400$ cách chọn.

Chọn được $3$ nữ và $2$ học sinh nam có: $C_{10}^3C_{10}^2 = 5400$ cách chọn.

Vậy có: $5400 + 5400 = 10800$ cách chọn.

2) Nếu trong $5$ học sinh phải có ít nhất $1$ học sinh nữ và $1$ học sinh nam thì có $4$ khả năng xảy ra:

+ Chọn được $1$ nam và $4$ nữ: có $C_{10}^1.C_{10}^4$ cách.

+ Chọn được $2$ nam và $3$ nữ: có $C_{10}^2.C_{10}^3$ cách.

+ Chọn được $3$ nam và $2$ nữ: có $C_{10}^3.C_{10}^2$ cách.

+ Chọn được $4$ nam và $1$ nữ: có $C_{10}^4.C_{10}^1$ cách.

Vậy tất cả có: $2.C_{10}^1.C_{10}^4 + 2.C_{10}^2.C_{10}^3 = 15000$ cách.

## Bài 3: Đội tuyển học sinh giỏi của một trường gồm $18$ em, trong đó có $7$ học sinh khối $12$, $6$ học sinh khối $11$, $5$ học sinh khối $10$. Hỏi có bao nhiêu cách cử $8$ học sinh trong đội đi dự trại hè sao cho mỗi khối có ít nhất một em được chọn.

Lời giải:

Tổng số cách chọn $8$ học sinh từ $18$ em của đội tuyển là: $C_{18}^8 = 43758.$

Số cách chọn $8$ em được chọn từ khối $12$ hoặc $11$: có $C_{13}^8$ cách.

Số cách chọn $8$ em được chọn từ khối $12$ hoặc $10$: có $C_{12}^8$ cách.

Số cách chọn $8$ em được chọn từ khối $11$ hoặc $10$: có $C_{11}^8$ cách.

Do mỗi khối có số học sinh đều nhỏ hơn $8$ nên không thể chọn $8$ học sinh ở mỗi khối.

Vậy số cách phải tìm là: $C_{18}^8 – \left( {C_{13}^8 + C_{12}^8 + C_{11}^8} \right) = 41811$ cách.

## Bài 4: Từ một tổ gồm $7$ học sinh nữ và $5$ học sinh nam cần chọn ra $6$ em trong đó số học sinh nữ phải nhỏ hơn $4.$ Hỏi có bao nhiêu cách chọn như vậy?

Lời giải:

Có $3$ khả năng:

+ $5$ nam và $1$ nữ: có $C_5^5.C_7^1$ cách.

+ $4$ nam và $2$ nữ: có $C_5^4.C_7^2$ cách.

+ $3$ nam và $3$ nữ: có $C_5^3.C_7^3$ cách.

Vậy tất cả có: $C_5^5.C_7^1 + C_5^4.C_7^2 + C_5^3.C_7^3$ $= 7 + 5.21 + 10.35 = 462$ cách.

## Bài 5: Trong một môn học, thầy giáo có $30$ câu hỏi khác nhau gồm $5$ câu hỏi khó, $10$ câu hỏi trung bình, $15$ câu hỏi dễ. Từ $30$ câu hỏi đó có thể lập được bao nhiêu đề kiểm tra, mỗi đề gồm $5$ câu hỏi khác nhau và nhất thiết phải có đủ $3$ loại câu hỏi (khó, trung bình, dễ) và số câu hỏi dễ không ít hơn $2.$

Lời giải:

Mỗi đề kiểm tra có số câu dễ là $2$ hoặc $3$, nên có các trường hợp sau:

+ Đề có $2$ câu dễ, $2$ câu trung bình, $1$ câu khó $\Rightarrow$ có $C_{15}^2.C_{10}^2.C_5^1$ đề.

+ Đề có $2$ câu dễ, $1$ câu trung bình, $2$ câu khó $\Rightarrow$ có $C_{15}^2.C_{10}^1.C_5^2$ đề.

+ Đề có $3$ câu dễ, $1$ câu trung bình, $1$ câu khó $\Rightarrow$ có $C_{15}^3.C_{10}^1.C_5^1$ đề.

Vậy tất cả có: $C_{15}^2.C_{10}^2.C_5^1 + C_{15}^2.C_{10}^1.C_5^2 + C_{13}^3.C_{10}^1.C_5^1$ $= 23625 + 10500 + 22750 = 56875$ đề.

## Bài 6: Một đội thanh niên tình nguyện có $15$ người, gồm $12$ nam và $3$ nữ. Hỏi có bao nhiêu cách phân công đội thanh niên tình nguyện đó về giúp đỡ $3$ tỉnh miền núi, sao cho mỗi tỉnh có $4$ nam và $1$ nữ.

Lời giải:

Có $C_3^1C_{12}^4$ cách phân công các thanh niên tình nguyện về tỉnh thứ nhất.

Với mỗi cách phân công các thanh niên tình nguyện về tỉnh thứ nhất, thì có $C_2^1C_8^4$ cách phân công các thanh niên tình nguyện về tỉnh thứ hai.

Với mỗi cách phân công các thanh niên tình nguyện về tỉnh thứ nhất và tỉnh thứ hai, thì có $C_1^1C_4^4$ cách phân công các thanh niên tình nguyện về tỉnh thứ ba.

Vậy tất cả có: $C_3^1C_{12}^4.C_2^1C_8^4.C_1^1C_4^4 = 207900$ cách phân công.

## Bài 7: Một đội văn nghệ có $15$ người gồm $10$ nam và $5$ nữ. Hỏi có bao nhiêu cách lập một nhóm đồng ca gồm $8$ người, biết rằng trong nhóm đó phải có ít nhất $3$ nữ.

Lời giải:

Ta có các trường hợp:

+ $3$ nữ và $5$ nam: có $C_5^3C_{10}^5 = 2520$ cách.

+ $4$ nữ và $4$ nam: có $C_5^4C_{10}^4 = 1050$ cách.

+ $5$ nữ và $3$ nam: có $C_5^5C_{10}^3 = 120$ cách.

Vậy tất cả có: $2520 + 1050 + 120 = 3690$ cách.

## Bài 8: Đội thanh niên xung kích của một trường phổ thông có $12$ học sinh, gồm $5$ học sinh lớp A, $4$ học sinh lớp B và $3$ học sinh lớp C. Cần chọn $4$ học sinh đi làm nhiệm vụ, sao cho $4$ học sinh này thuộc không quá $2$ trong $3$ lớp trên. Hỏi có bao nhiêu cách chọn như vậy?

Lời giải:

Số cách chọn $4$ học sinh từ $12$ học sinh đã cho là: $C_{12}^4 = 495.$

Số cách chọn $4$ học sinh mà mỗi lớp có ít nhất một em được tính như sau:

+ Lớp A có $2$ học sinh, các lớp B, C mỗi lớp $1$ học sinh.

$\Rightarrow$ Số cách chọn là: $C_5^2C_4^1C_3^1 = 120.$

+ Lớp B có $2$ học sinh, các lớp A, C mỗi lớp $1$ học sinh:

$\Rightarrow$ Số cách chọn là: $C_5^1C_4^2C_3^1 = 90.$

+ Lớp C có $2$ học sinh, các lớp A, B mỗi lớp $1$ học sinh:

$\Rightarrow$ Số cách chọn là: $C_5^1C_4^1C_3^2 = 60.$

Số cách chọn $4$ học sinh mà mỗi lớp có ít nhất một học sinh là:

$120 + 90 + 60 = 270.$

Vậy có: $495 – 270 = 225$ cách chọn $4$ học sinh đi làm nhiệm vụ mà $4$ học sinh này thuộc không quá $2$ trong $3$ lớp.

## Bài 9: Từ một nhóm gồm $15$ học sinh khối A, $10$ học sinh khối B, $5$ học sinh khối C, chọn ra $15$ học sinh sao cho có ít nhất $5$ học sinh khối A và đúng $2$ học sinh khối C. Tính số cách chọn.

Lời giải:

Chọn $15$ học sinh có đúng $2$ học sinh khối C và $13$ học sinh tùy ý trong hai khối A và B có $C_5^2C_{25}^{13}$ cách chọn.

Trong các cách chọn đó ta xét chọn ra $15$ học sinh có đúng $2$ học sinh khối C và nhiều nhất $4$ học sinh khối A có các trường hợp sau:

+ Chọn $2$ học sinh khối C, $4$ học sinh khối A và $9$ học sinh khối B:

Có $C_5^2C_{15}^4C_{10}^9$ cách chọn.

+ Chọn $2$ học sinh khối C, $5$ học sinh khối A và $10$ học sinh khối B:

Có $C_5^2C_{15}^5C_{10}^{10}$ cách chọn.

Vậy loại này có: $C_5^2C_{15}^4C_{10}^9 + C_5^2C_{15}^5C_{10}^{10} = 166530$ cách chọn.

Vậy có: $C_5^2C_{25}^{13} – 166530 = 51836470$ cách chọn ra $15$ học sinh sao cho có ít $5$ học sinh khối A và đúng $2$ học sinh khối C.

## Bài 10: Cho tập hợp $A = \{ 1,2,3,4,5,6,7,8\} .$ Có bao nhiêu tập con $X$ của tập $A$ thoả điều kiện $X$ chứa $1$ và không chứa $2.$

Lời giải:

Tập hợp $X = \{ 1\} \cup Y$, với $Y \subset \{ 3;4;5;6;7;8\} .$

Do đó số tập $X$ bằng số tập con $Y$ của tập hợp $\{ 3;4;5;6;7;8\} .$

Mà số tập con $Y$ của $\{ 3;4;5;6;7;8\}$ là ${2^6} = 64.$

Do đó số tập con $X$ của tập $A$ thỏa điều kiện chứa $1$ và không chứa $2$ là: $64.$

## Bài 11: Một hộp đựng $4$ viên bị đỏ, $5$ viên bị trắng và $6$ viên bi vàng. Người ta chọn ra $4$ viên bi từ hộp đó. Hỏi có bao nhiêu cách chọn để trong số bi lấy ra không có đủ cả $3$ màu?

Lời giải:

Gọi $m$ là số cách chọn $4$ viên bi tùy ý.

Gọi $n$ là số cách chọn $4$ viên bi đủ cả $3$ màu.

Gọi $p$ là số cách chọn $4$ viên bi không đủ $3$ màu.

Khi đó: $p = m – n.$

Ta có: $m = C_{15}^4 = 1365$ cách.

Tính $n$: chọn $4$ viên bi đủ cả $3$ màu thì $4$ viên bi đó có thể là $1$ bi đỏ, $1$ bi trắng, $2$ bi vàng hoặc $1$ bi đỏ, $2$ bi trắng, $1$ bi vàng hoặc $2$ bi đỏ, $1$ bi trắng, $1$ bi vàng.

Suy ra: $n = C_4^1C_5^1C_6^2 + C_4^1C_5^2C_6^1 + C_4^2C_5^1C_6^1 = 720$ cách.

Vậy số cách chọn $4$ bi không đủ $3$ màu là: $p = m – n$ $= 1365 – 720 = 645$ cách.

## Bài 12: Một lớp có $30$ học sinh nam và $15$ học sinh nữ. Có $6$ học sinh được chọn ra để lập một tốp ca. Hỏi có bao nhiêu cách chọn khác nhau nếu:

1) Phải có ít nhất là $2$ nữ.

2) Chọn tuỳ ý.

Lời giải:

1) Trường hợp 1: Chọn được $2$ nữ và $4$ nam có: $C_{15}^2.C_{30}^4$ cách chọn.

Trường hợp 2: Chọn được $3$ nữ và $3$ nam có: $C_{15}^3.C_{30}^3$ cách chọn.

Trường hợp 3: Chọn được $4$ nữ và $2$ nam có: $C_{15}^4.C_{30}^2$ cách chọn.

Trường hợp 4: Chọn được $5$ nữ và $1$ nam có: $C_{15}^5.C_{30}^1$ cách chọn.

Trường hợp 5: Chọn được $6$ nữ có: $C_{15}^6$ cách chọn.

Vậy theo quy tắc cộng có: $C_{15}^2.C_{30}^4 + C_{15}^3.C_{30}^3 + C_{15}^4.C_{30}^2 + C_{15}^5.C_{30}^1 + C_{15}^6$ $= 5413695$ cách chọn.

2) Số cách chọn là: $C_{45}^6 = 8145060.$

## Bài 13: Có $5$ nhà toán học nam, $3$ nhà toán học nữ và $4$ nhà vật lí nam. Lập một đoàn công tác $3$ người cần có cả nam và nữ, cần có cả nhà toán học và nhà vật lí. Hỏi có bao nhiều cách?

Lời giải:

Trường hợp 1: Chọn $1$ nhà toán học nữ, $1$ nhà toán học nam, $1$ nhà vật lý có: $C_3^1C_5^1C_4^1 = 60$ cách chọn.

Trường hợp 2: Chọn được $1$ nhà toán học nữ và $2$ nhà vật lý có: $C_3^1C_4^2 = 18$ cách chọn.

Trường hợp 3: Chọn được $2$ nhà toán học nữ và $1$ nhà vật lý có: $C_3^2C_4^1 = 12$ cách chọn.

Vậy theo quy tắc cộng có: $60 + 18+ 12 = 90$ cách chọn.

## Bài 14: Một đội văn nghệ có $20$ người, trong đó có $10$ nam và $10$ nữ. Hỏi có bao nhiêu cách chọn ra $5$ người sao cho:

## Bài tập 1. Có đúng $2$ nam trong $5$ người đó.

## Bài tập 2. Có ít nhất $2$ nam và ít nhất $1$ nữ trong $5$ người đó.

Lời giải:

1) Số cách chọn $5$ người trong đó có đúng $2$ nam là: $C_{10}^2C_{10}^3 = 5400$ cách.

2) Chọn ra $5$ người có ít nhất $2$ nam và ít nhất $1$ nữ xảy ra các trường hợp sau:

+ Trường hợp 1: Chọn được $2$ nam và $3$ nữ có $C_{10}^2C_{10}^3$ cách chọn.

+ Trường hợp 2: Chọn được $3$ nam và $2$ nữ có $C_{10}^3C_{10}^2$ cách chọn.

+ Trường hợp 3: Chọn được $4$ nam và $1$ nữ có $C_{10}^4C_{10}^1$ cách chọn.

Vậy theo quy tắc cộng có: $C_{10}^2C_{10}^3 + C_{10}^3C_{10}^2 + C_{10}^4C_{10}^1 = 12900$ cách chọn ra $5$ người trong đó có ít nhất $2$ nam và $1$ nữ.

## Bài 15: Có $9$ viên bi xanh, $5$ viên bi đỏ, $4$ viên bi vàng có kích thước đôi một khác nhau.

## Bài tập 1. Có bao nhiêu cách chọn ra $6$ viên bi, trong đó có đúng $2$ viên bi đỏ.

## Bài tập 2. Có bao nhiêu cách chọn ra $6$ viên bi, trong đó số bi xanh bằng số bi đỏ.

Lời giải:

## Bài tập 1. Có: $C_5^2$ cách chọn ra $2$ viên bi đỏ.

$C_{13}^4$ cách chọn ra $4$ viên bi còn lại.

Vậy có: $C_5^2.C_{1.3}^4 = 7150$ cách chọn.

## Bài tập 2. Có các trường hợp xảy ra:

+ $3$ xanh, $3$ đỏ, $0$ vàng $\to$ có $C_9^3.C_5^3$ cách.

+ $2$ xanh, $2$ đỏ, $2$ vàng $\to$ có $C_9^2.C_5^2.C_4^2$ cách.

+ $1$ xanh, $1$ đỏ, $4$ vàng $\to$ có $C_9^1.C_5^1.C_4^4$ cách.

Vậy có tất cả: $C_9^3.C_5^3 + C_9^2.C_5^2.C_4^2 + C_9^1.C_5^1.C_4^4 = 3045$ cách.

## Bài 16: Một đồn cảnh sát khu vực có $9$ người. Trong ngày, cần cử $3$ người làm nhiệm vụ ở địa điểm A, $2$ người ở địa điểm B, còn $4$ người thường trực tại đồn. Hỏi có bao nhiêu cách phân công?

Lời giải:

Chọn $3$ người làm nhiệm vụ ở địa điểm A có $C_9^3$ cách chọn.

Chọn $2$ người làm nhiệm vụ ở địa điểm B có $C_6^2$ cách chọn.

Chọn $4$ người thường trực tại đồn có $C_4^4$ cách chọn.

Vậy theo quy tắc nhân có: $C_9^3C_6^2C_4^4 = 1260$ cách phân công.

## Bài 17: Một lớp học có $20$ học sinh, trong đó có $2$ cán bộ lớp. Hỏi có bao nhiêu cách cử $3$ người đi dự hội nghị Hội sinh viên của trường sao cho trong $3$ người đó có ít nhất một cán bộ lớp.

Lời giải:

Số cách chọn $3$ người tùy ý là: $C_{20}^3$ cách chọn.

Số cách chọn $3$ người mà không có cán bộ lớp là: $C_{18}^3$ cách chọn.

Vậy số cách chọn ra $3$ người có ít nhất $1$ cán bộ lớp là: $C_{20}^3 – C_{18}^3 = 324$ cách.

## Bài 18: Một lớp học sinh mẫu giáo gồm $15$ em, trong đó có $9$ em nam, $6$ em nữ. Cô giáo chủ nhiệm muốn chọn một nhóm $5$ em để tham dự trò chơi gồm $3$ em nam và $2$ em nữ. Hỏi có bao nhiêu cách chọn?

Lời giải:

Chọn $3$ em nam trong $9$ em nam có: $C_9^3$ cách chọn.

Chọn $2$ em nữ trong $6$ em nữ có: $C_6^3$ cách chọn.

Vậy theo quy tắc nhân có: $C_9^3C_6^3 = 1680$ cách chọn.

## Bài 19: Một đội văn nghệ có $10$ người, trong đó có $6$ nữ và $4$ nam.

## Bài tập 1. Có bao nhiêu cách chia đội văn nghệ thành hai nhóm có số người bằng nhau và mỗi nhóm có số nữ như nhau.

## Bài tập 2. Có bao nhiêu cách chọn ra $5$ người mà trong đó không có quá $1$ nam.

Lời giải:

## Bài tập 1. Chia đội văn nghệ thành hai nhóm có số người bằng nhau và mỗi nhóm có số nữ như nhau tức là chia mỗi nhóm có $5$ người mà trong đó có $3$ nữ và $2$ nam $\Rightarrow$ số cách chia là: $C_6^3.C_4^2 = 120.$

## Bài tập 2. Có hai trường hợp xảy ra:

Trường hợp 1: Chọn ra $5$ người mà không có nam có: $C_6^5 = 6$ cách chọn.

Trường hợp 2: Chọn ra $5$ người mà có $1$ nam (và $4$ nữ) có: $C_6^4.C_4^1 = 60$ cách chọn.

Vậy số cách chọn ra $5$ người mà có không quá $1$ nam là: $6 + 60 = 66.$

## Bài 20: Từ một nhóm học sinh gồm $7$ nam và $6$ nữ, thầy giáo cần chọn ra $5$ em tham dự lễ mít tinh tại trường với yêu cầu có cả nam và nữ. Hỏi có bao nhiêu cách chọn?

Lời giải:

Số cách chọn $5$ em từ $13$ em là: $C_{13}^5 = 1287.$

Số cách chọn $5$ em toàn nam là: $C_7^5 = 21.$

Số cách chọn $5$ em toàn nữ là: $C_6^{ \cdot 5} = 6.$

Vậy số cách chọn $5$ em có cả nam và nữ là: $1287 – (21 + 6) = 1260.$

## Bài 21: Trong số $16$ học sinh có $3$ học sinh giỏi, $5$ khá, $8$ trung bình. Có bao nhiêu cách chia số học sinh đó thành $2$ tổ, mỗi tổ có $8$ người sao cho ở mỗi tổ đều có học sinh giỏi và mỗi tổ có ít nhất $2$ học sinh khá.

Lời giải:

Mỗi tổ có $1$ hoặc $2$ học sinh giỏi. Vì không phân biệt thứ tự của $2$ tổ nên số cách chia phải tìm là số cách tạo thành một tổ có $8$ học sinh trong đó phải có $1$ học sinh giỏi và ít nhất $2$ học sinh khá. Các học sinh còn lại tạo thành tổ thứ hai.

+ Trường hợp 1: Có $2$ học sinh khá:

Có $3$ cách chọn $1$ học sinh giỏi.

Có $C_5^2 = 10$ cách chọn $2$ học sinh khá.

Có $C_8^5 = 56$ cách chọn $5$ học sinh trung bình.

$\Rightarrow$ Có: $3.10.56 = 1680$ cách.

+ Trường hợp 2: Có $3$ học sinh khá.

Có $3$ cách chọn $1$ học sinh giỏi.

Có $C_5^3 = 10$ cách chọn $3$ học sinh khá.

Có $C_8^4 = 70$ cách chọn $4$ học sinh trung bình.

$\Rightarrow$ Có: $3.10.70 = 2100$ cách.

Vậy có tất cả: $1680 + 2100 = 3780$ cách.

## Bài 22: Từ các chữ số $1$, $2$, $3$, $4$, $5$, $6$, $7$, $8$, $9$ có thể lập được bao nhiêu số có $9$ chữ số khác nhau mà chữ số $9$ đứng ở vị trí chính giữa?

Lời giải:

Ta chỉ có $1$ cách chọn vị trí cho chữ số $9.$

Khi đó số cách xếp $8$ chữ số còn lại là $8!.$

Vậy tất cả có: $8! = 40320$ số.

## Bài 23: Cho $A$ là một hợp có $20$ phần tử.

## Bài tập 1. Có bao nhiêu tập hợp con của $A$?

## Bài tập 2. Có bao nhiêu tập hợp con khác rỗng của $A$ mà có số phần tử là số chẵn?

Lời giải:

## Bài tập 1. Số tập con của $A$ là: $C_{20}^0 + C_{20}^1 + C_{20}^2 + \ldots + C_{20}^{20} = {2^{20}}.$

## Bài tập 2. Số tập con khác rỗng của $A$ có số phần tử chẵn là:

$T = C_{20}^2 + C_{20}^4 + \ldots + C_{20}^{20}.$

Ta có: $0 = {(1 – 1)^{20}}$ $= C_{20}^0 – C_{20}^1 + C_{20}^2 – \ldots + C_{20}^{20}.$

$\Rightarrow C_{20}^0 + C_{20}^2 + C_{20}^4 + \ldots + C_{20}^{20}$ $= C_{20}^1 + C_{20}^3 + \ldots + C_{20}^{19}.$

$\Rightarrow C_{20}^0 + C_{20}^1 + C_{20}^2 + \ldots + C_{20}^{20}$ $= 2\left( {C_{20}^0 + C_{20}^2 + C_{20}^4 + \ldots + C_{20}^{20}} \right).$

$\Rightarrow T = C_{20}^2 + C_{20}^4 + \ldots + C_{20}^{20}$ $= \frac{{{2^{20}}}}{2} – C_{20}^0$ $= {2^{19}} – 1.$

## Bài 24: Có $12$ viên bi khác nhau. Hỏi có bao nhiêu cách sắp xếp chúng vào $6$ chiếc hộp giống nhau, mỗi hộp có hai viên bi?.

Lời giải:

Giả sử $6$ hộp này khác nhau.

Chọn $2$ viên bi xếp vào hộp thứ nhất có $C_{12}^2$ cách.

Chọn $2$ viên bi tiếp theo xếp vào hộp thứ hai có $C_{10}^2$ cách.

Chọn $2$ viên bi tiếp theo xếp vào hộp thứ ba có $C_8^2$ cách.

Chọn $2$ viên bi tiếp theo xếp vào hộp thứ tư có $C_6^2$ cách.

Chọn $2$ viên bi tiếp theo xếp vào hộp thứ năm có $C_4^2$ cách.

Chọn $2$ viên bi tiếp theo xếp vào hộp thứ sáu có $C_2^2$ cách.

Vậy có $C_{12}^2C_{10}^2C_8^2C_6^2C_4^2C_2^2 = 7484400$ cách.

Nhưng vì $6$ hộp này giống nhau nên số cách sắp xếp thỏa yêu cầu bài toán là $\frac{{7484400}}{{6!}} = 10395$ cách.

## Bài 25: Có hai chuồng gà, chuồng $1$ nhốt $3$ gà trống và $4$ gà mái, chuồng $2$ nhốt $4$ gà trống và $5$ gà mái. Hỏi có bao nhiêu cách bắt một lần $3$ con gà từ một trong hai chuồng đã cho, trong đó có hai gà trống và một gà mái?.

Lời giải:

+ Trường hợp $1$: Bắt được $3$ con gà từ chuồng $1$ trong đó có $2$ con gà trống và một gà mái.

Bắt $2$ con gà trống có $C_3^2 = 3$ cách.

Bắt $1$ con gà mái có $C_4^1 = 4$ cách.

Suy ra trường hợp này có $3.4 = 12$ cách.

+ Trường hợp 2: Bắt được $3$ con gà từ chuồng $2$ trong đó có $2$ con gà trống và $1$ gà mái.

Bắt $2$ con gà trống có $C_4^2 = 6$ cách.

Bắt $1$ con gà mái có $C_5^1 = 5$ cách.

Suy ra trường hợp này có $6.5 = 30$ cách.

Vậy tất cả có $12 + 30 = 42$ cách.

## Bài 26: Có bao nhiêu cách chia một lớp có $50$ học sinh (gồm $30$ nam và $20$ nữ) thành $5$ tổ mỗi tổ $6$ nam và $4$ nữ.

Lời giải:

Chọn $6$ nam và $4$ nữ của tổ $1$ có $C_{30}^6C_{20}^4$ cách chọn.

Chọn $6$ nam và $4$ nữ của tổ $2$ có $C_{24}^6C_{16}^4$ cách chọn.

Chọn $6$ nam và $4$ nữ của tổ $3$ có $C_{18}^6C_{12}^4$ cách chọn.

Chọn $6$ nam và $4$ nữ của tổ $4$ có $C_{12}^6C_8^4$ cách chọn.

Chọn $6$ nam và $4$ nữ của tổ $4$ có $C_6^6C_4^4$ cách chọn.

Vậy có $C_{30}^6C_{20}^4C_{24}^6C_{16}^4C_{18}^6C_{12}^4C_{12}^6C_8^4C_6^6C_4^4$ cách chia lớp thành $5$ tổ mỗi tổ có $6$ nam và $4$ nữ.

## Bài 27: Một ban văn nghệ gồm $10$ nam và $3$ nữ. Chọn $3$ nam và $3$ nữ ghép thành $3$ cặp múa đôi. Hỏi có bao nhiêu cách chọn như trên?.

Lời giải:

Chọn $3$ nam trong $10$ nam có: $C_{10}^3 = 120$ cách chọn.

Chọn $3$ nữ trong $3$ nữ có $1$ cách chọn.

Mỗi cách chọn $3$ nam và $3$ nữ trên thì có $3! = 6$ cách ghép $3$ nam và $3$ nữ thành $3$ cặp múa.

Vậy có: $120.1.6 = 720$ cách chọn.

Cách khác:

Vì nữ chỉ có $3$ người nên số cách chọn để ghép thành $3$ cặp múa là số cách chọn có thứ tự $3$ nam trong $10$ nam.

Vậy số cách chọn là: $A_{10}^3 = 720$ cách.

## Bài 28: Một hộp có chứa các viên bi có kích thước giống nhau gồm $9$ bi đỏ, $6$ bi xanh, $5$ bi vàng. Có bao nhiêu cách chọn $12$ bi trong đó có đủ cả $3$ màu.

Lời giải:

Tổng tất cả có $20$ viên bi trong hộp.

Số cách chọn $12$ viên bi bất kỳ trong $20$ viên bi là: $C_{20}^{12} = 125970.$

Trong số các cách chọn trên ta đi tính số cách chọn $12$ viên bi trong đó không có đủ $3$ màu.

Nhận xét rằng không có cách chọn $12$ viên bi nào thuộc cùng một màu, do đó:

Số cách chọn $12$ viên bi lấy trong $15$ viên bi gồm $9$ bi đỏ và $6$ bi xanh là: $C_{15}^{12} = 455$ cách.

Số cách chọn $12$ viên bi lấy trong $14$ viên bi gồm $9$ bi đỏ và $5$ bi vàng là: $C_{14}^{12} = 91$ cách.

Suy ra có: $455 + 91 = 546$ cách chọn $12$ viên bi trong đó không có đủ cả $3$ màu.

Vậy có $125970 – 546 = 125424$ cách chọn $12$ viên bi trong đó có đủ cả $3$ màu.

## Bài 29: Có $21$ sinh viên nam và $9$ sinh viên nữ được phân công về $3$ trường A, B, C. Có bao nhiêu cách phân công như vậy sao cho số nam bằng nhau và số nữ bằng nhau?

Lời giải:

Chọn $7$ nam và $3$ nữ nhóm thứ nhất và phân công về $1$ trường có $C_{21}^7C_9^3$ cách.

Chọn $7$ nam và $3$ nữ nhóm thứ hai và phân công về $1$ trường có $C_{14}^7C_6^3$ cách.

Chọn $7$ nam và $3$ nữ còn lại là nhóm thứ ba và phân công về $1$ trường có $1$ cách.

Vậy có $C_{21}^7C_9^3C_{14}^7C_6^3$ cách phân công $3$ nhóm về $3$ trường A, B, C.

## Bài 30: Có $10$ sinh viên môn Toán trong đó có $7$ sinh viên nam và có $6$ sinh viên Lý đều là nam. Hỏi có bao nhiêu cách chọn $3$ sinh viên trong đó vừa có toán vừa có lý, vừa có nam, vừa có nữ.

Lời giải:

Xét các trường hợp sau:

+ Chọn được $1$ nam sinh viên Toán và $1$ nữ sinh viên Toán và $1$ nam sinh viên Lý.

Chọn $1$ nam sinh viên Toán có $7$ cách chọn.

Chọn $1$ nữ sinh viên Toán có $3$ cách chọn.

Chọn $1$ nam sinh viên Lý có $6$ cách chọn.

Suy ra trường hợp này có: $7.3.6 = 126$ cách.

+ Chọn được $2$ nữ sinh viên Toán và $1$ nam sinh viên Lý.

Chọn $2$ nữ sinh viên Toán có $C_3^2 = 3$ cách chọn.

Chọn $1$ nam sinh viên Lý có $6$ cách chọn.

Suy ra trường hợp này có: $3.6 = 18$ cách.

+ Chọn được $1$ nữ sinh viên Toán và $2$ nam sinh viên Lý.

Chọn $1$ nữ sinh viên Toán có $3$ cách chọn.

Chọn $2$ nam sinh viên Lý có $C_6^2 = 15$ cách chọn.

Suy ra trường hợp này có: $3.15 = 45$ cách.

Vậy tất cả có: $126 + 18+ 45 = 189$ cách chọn $3$ sinh viên trong đó vừa có toán vừa có lý, vừa có nam, vừa có nữ.

## Bài 31: Trong một bản đồ được lập theo kỹ thuật số của thành phố X, mỗi căn nhà trong thành phố đều được lập địa chỉ và “địa chỉ số nhà” của mỗi căn nhà là một dãy gồm $16$ chữ cái lấy từ hai chữ $0$ và $1$ (ví dụ: $0000110000111100$). Hỏi thành phố X có bao nhiêu căn nhà.

Lời giải:

Số căn nhà trong thành phố X là số địa chỉ được lập theo kỹ thuật số.

Do mỗi địa chỉ có $16$ chữ, mà mỗi chữ có $2$ cách lấy từ hai chữ $0$ hoặc $1.$

Vậy có ${2^{16}}$ căn nhà.

## Bài 32: Dãy $\left( {{x_1},{x_2},{x_3}, \ldots ,{x_{10}}} \right)$ trong đó mỗi kí tự ${x_i}$ chỉ nhận giá trị $0$ hoặc $1$ được gọi là dãy nhị phân $10$ bit.

a) Có bao nhiêu dãy nhị phân $10$ bit.

b) Có bao nhiêu dãy nhị phân $10$ bit trong đó có ít nhất $3$ ký tự $0$ và ít nhất $3$ kí tự $1.$

Lời giải:

a) Dãy nhị phân gồm $10$ bit, mỗi bit có $2$ cách chọn giá trị $0$ hoặc $1.$

Vậy có tất cả ${2^{10}} = 1024$ dãy nhị phân $10$ bit.

b) Giả sử dãy nhị phân $10$ bit có các bit tương ứng với $10$ ô trống: ▯▯▯▯▯▯▯▯▯▯.

Xét các trường hợp sau:

+ Dãy gồm $3$ ký tự $0$ và $7$ ký tự $1:$

Có $C_{10}^3$ cách chọn $3$ ô trống để đặt $3$ ký tự $0.$

Có $1$ cách chọn $7$ ô trống để đặt $7$ ký tự $1.$

Suy ra trường hợp này có: $1.C_{10}^3 = 120$ dãy.

+ Dãy gồm $4$ ký tự $0$ và $4$ ký tự $1:$

Có $C_{10}^4$ cách chọn $4$ ô trống để đặt $4$ ký tự $0.$

Có $1$ cách chọn $6$ ô trống để đặt $6$ ký tự $1.$

Suy ra trường hợp này có: $1.C_{10}^4 = 210$ dãy.

+ Dãy gồm $5$ ký tự $0$ và $5$ ký tự $1:$

Có $C_{10}^5$ cách chọn $5$ ô trống để đặt $5$ ký tự $0.$

Có $1$ cách chọn $5$ ô trống để đặt $5$ ký tự $1.$

Suy ra trường hợp này có: $1.C_{10}^5 = 252$ dãy.

+ Dãy gồm $6$ ký tự $0$ và $4$ ký tự $1:$

Có $C_{10}^6$ cách chọn $6$ ô trống để đặt $4$ ký tự $0.$

Có $1$ cách chọn $4$ ô trống để đặt $4$ ký tự $1.$

Suy ra trường hợp này có $1.C_{10}^6 = 210$ dãy.

+ Dãy gồm $7$ ký tự $0$ và $3$ ký tự $1:$

Có $C_{10}^7$ cách chọn $7$ ô trống để đặt $7$ ký tự $0.$

Có $1$ cách chọn $3$ ô trống để đặt $3$ ký tự $1.$

Suy ra trường hợp này có: $1.C_{10}^7 = 120$ dãy.

Vậy tất cả có: $120 + 210 + 252 + 210 + 120 = 912$ dãy $10$ bit trong đó có ít nhất $3$ ký tự $0$ và ít nhất $3$ ký tự $1.$

## Bài 33: Gieo $3$ con súc sắc cân đối và đồng chất, có bao nhiêu trường hợp:

a) Ba mặt khác nhau?

b) Chỉ có một mặt là số $2$, hai mặt còn lại khác nhau và khác $2$?

c) Chỉ có một mặt là số $2$, hai mặt còn lại tùy ý và khác $2$?

Lời giải:

Gọi $(a;b;c)$ với $1 \le a,b,c \le 6$ là kết quả xuất hiện số chấm trên $3$ con xúc xắc của phép thử trên.

a) Số trường hợp để $a$, $b$, $c$ khác nhau là số cách chọn có thứ tự $3$ chữ số từ các chữ số $1$, $2$, $3$, $4$, $5$, $6.$

Vậy số trường hợp để ba mặt khác nhau là: $A_6^3 = 120.$

b) Mặt có chữ số $2$ có $3$ trường hợp xảy ra (có thể $a= 2$, hoặc $b = 2$ hoặc $c=2$).

Mỗi trường hợp trên có $A_5^2 = 20$ trường hợp xảy ra với số chấm của $2$ con súc sắc còn lại.

Vậy có: $3.20 = 60$ trường hợp.

c) Mặt có chữ số $2$ có $3$ trường hợp xảy ra (có thể $a = 2$, hoặc $b = 2$ hoặc $c =2$).

Do các mặt còn lại chỉ cần khác $2$ nên có $5.5 = 25$ trường hợp xuất hiện số chấm trên $2$ con súc sắc còn lại.

Vậy có: $3.25 = 75$ trường hợp.

## Bài 34: Một đội văn nghệ có $20$ người, trong đó có $10$ nam và $10$ nữ. Hỏi có bao nhiêu cách chọn ra $5$ người, sao cho:

a) Có đúng $2$ nam trong $5$ người đó.

b) Có ít nhất $3$ nam trong $5$ người đó?

Lời giải:

a) Chọn $5$ người trong đó có đúng $2$ nam, thì $3$ người còn lại là nữ.

Vậy số cách chọn là: $C_{10}^2C_{10}^3 = 5400.$

b) Ta xét các trường hợp sau:

Chọn được $3$ nam và $2$ nữ có: $C_{10}^3C_{10}^2 = 5400$ cách chọn.

Chọn được $4$ nam và $1$ nữ có: $C_{10}^4C_{10}^1 = 2100$ cách chọn.

Chọn được đúng $5$ nam có: $C_{10}^5 = 252$ cách chọn.

Vậy tất cả có: $5400 + 2100 + 252 = 7752$ cách chọn.

## Bài 35: Hội đồng quản trị của một công ty gồm $12$ người, trong đó có $5$ nữ. Từ hội đồng quản trị đó người ta bầu ra $1$ chủ tịch hội đồng quản trị, $1$ phó chủ tịch hội đồng quản trị và $2$ ủy viên. Hỏi có mấy cách bầu sao cho trong $4$ người được bầu phải có nữ.

Lời giải:

+ Loại 1: bầu $4$ người tùy ý (không phân biệt nam, nữ).

Bước 1: bầu chủ tịch và phó chủ tịch có $A_{12}^2$ cách.

Bước 2: bầu $2$ ủy viên có $C_{10}^2$ cách.

Suy ra có $A_{12}^2.C_{10}^2$ cách bầu loại 1.

+ Loại 2: bầu $4$ người toàn nam.

Bước 1: bầu chủ tịch và phó chủ tịch có $A_7^2$ cách.

Bước 2: bầu $2$ ủy viên có $C_5^2$ cách.

Suy ra có $A_7^2.C_5^2$ cách bầu loại 2.

Vậy có $A_{12}^2.C_{10}^2 – A_7^2.C_5^2 = 5520$ cách bầu $4$ người trong đó luôn có nữ.

## Bài 36: Có $5$ học sinh trong đó có An và Bình. Hỏi có bao nhiêu cách sắp xếp $5$ học sinh này lên một đoàn tàu gồm $8$ toa, biết rằng:

a) $5$ học sinh cùng lên một toa.

b) $5$ học sinh lên $5$ toa đầu và mỗi toa có $1$ người.

c) $5$ học sinh lên $5$ toa khác nhau.

d) An và Bình lên cùng một toa đầu tiên.

e) An và Bình lên cùng một toa ngoài ra không có học sinh nào khác lên toa này.

Lời giải:

a) Số cách chọn $1$ toa tàu bất kỳ là $8$ cách.

Mỗi cách chọn toa tàu có $1$ cách để $5$ học sinh cùng lên tọa đó.

Vậy có $8$ cách để $5$ học sinh cùng lên một toa.

b) Mỗi cách sắp xếp $5$ học sinh lên $5$ toa đầu và mỗi toa có $1$ người là một hoán vị của $5$ học sinh.

Vậy số cách sắp xếp là $5! = 120.$

c) Mỗi cách sắp xếp $5$ học sinh lên $5$ toa khác nhau là một cách chọn có thứ tự $5$ toa tàu trong $8$ toa.

Vậy số cách xếp là: $A_8^5 = 6720.$

d) An và Bình lên toa đầu tiên có $1$ cách.

Còn $3$ học sinh còn lại lên các toa tùy ý, để tính số cách xếp $3$ học sinh này ta xét các trường hợp sau:

$3$ học sinh cùng lên một toa thì có: $C_8^1 = 8$ cách.

Mỗi học sinh lên một toa khác nhau có $A_8^3 = 336$ cách.

Một toa có $2$ học sinh và $1$ toa có $1$ học sinh:

Chọn $2$ học sinh có $C_3^2 = 3$ cách (nhóm 1).

Chọn $1$ học sinh còn lại có $1$ cách (nhóm 2).

Chọn $2$ toa bất kỳ để xếp $2$ nhóm trên có: $A_8^2 = 56$ cách.

Suy ra có: $3.1.56 = 168$ cách.

Vậy tất cả có: $8 + 336 + 168 = 512$ cách.

e) An và Bình lên cùng một toa có $8$ cách chọn.

Còn $3$ học sinh còn lại lên các toa tùy ý khác toa mà An và Bình đã lên, để tính số cách xếp $3$ học sinh này ta xét các trường hợp sau:

$3$ học sinh cùng lên một toa thì có: $C_7^1 = 7$ cách.

Mỗi học sinh lên một toa khác nhau có $A_7^3 = 210$ cách.

Một toa có $2$ học sinh và $1$ toa có $1$ học sinh:

Chọn $2$ học sinh có $C_3^2 = 3$ cách (nhóm 1).

Chọn $1$ học sinh còn lại có $1$ cách (nhóm 2).

Chọn $2$ toa bất kỳ để xếp $2$ nhóm trên có: $A_7^2 = 42$ cách.

Suy ra có: $3.1.42 = 126$ cách.

Suy ra có: $7 + 210 + 126 = 343$ cách xếp $3$ học sinh còn lại.

Vậy số cách xếp là: $8.343 = 2744$ cách.