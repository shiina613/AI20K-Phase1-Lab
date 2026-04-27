# Phương pháp tìm nguyên hàm các hàm số lượng giác (Phần 2)

<!-- chunk:0 level:0 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-2.html -->
Bài viết trình bày phương pháp tìm nguyên hàm các hàm số lượng giác, đây là dạng nguyên hàm thường gặp trong các đề thi THPT Quốc gia, đề tuyển sinh Đại học – Cao đẳng.

**XEM LẠI PHẦN 1**: Phương pháp tìm nguyên hàm các hàm số lượng giác (Phần 1)

**Phương pháp 2: Xác định nguyên hàm các hàm số lượng giác bằng cách sử dụng các phép biến đổi lượng giác.

****Phương pháp chung**: Sử dụng các phép biến đổi lượng giác đưa biểu thức dưới dấu tích phân về dạng quen thuộc. Các phép biến đổi thường dùng bao gồm:

+ Phép biến đổi tích thành tổng.

+ Hạ bậc.

+ Các kỹ thuật biến đổi khác.

<!-- chunk:1 level:2 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-2.html -->
## Dạng 1: Sử dụng phép biến đổi tích thành tổng.
Cách giải: Ở đây chúng ta nhớ lại các công thức lượng giác sau:

$\cos x\cos y = \frac{1}{2}\left[ {\cos (x + y) + \cos (x – y)} \right].$

$\sin x\sin y = \frac{1}{2}\left[ {\cos (x – y) – \cos (x + y)} \right].$

$\sin x\cos y = \frac{1}{2}\left[ {\sin (x + y) + \sin (x – y)} \right].$

$\cos x\sin y = \frac{1}{2}\left[ {\sin (x + y) – \sin (x – y)} \right].$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-2.html -->
## Ví dụ 11: Tìm họ nguyên hàm của hàm số: $f(x) = \cos 3x.\cos 5x.$

Sử dụng các phép biến đổi tích thành tổng, ta được: $f(x) = \frac{1}{2}(\cos 8x + \cos 2x).$

Khi đó: $F\left( x \right) = \frac{1}{2}\int {\left( {\cos 8x + \cos 2x} \right)dx}$ $= \frac{1}{2}\left( {\frac{1}{8}\sin 8x + \frac{1}{2}\sin 2x} \right) + C.$

Chú ý: Nếu hàm $f(x)$ là tích của nhiều hơn $2$ hàm số lượng giác ta thực hiện phép biến đổi dần, cụ thể ta đi xem xét ví dụ sau:

<!-- chunk:3 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-2.html -->
## Ví dụ 12: Tìm họ nguyên hàm của hàm số: $f(x) = \cos x.\sin 2x.\cos 3x.$

Sử dụng các phép biến đổi tích thành tổng, ta được: $f(x) = \frac{1}{2}(\sin 3x + \sin x)\cos 3x$ $= \frac{1}{2}(\sin 3x.\cos 3x + \cos 3x.\sin x)$ $= \frac{1}{2}\left[ {\frac{1}{2}\sin 6x + \frac{1}{2}(\sin 4x – \sin 2x)} \right]$ $= \frac{1}{4}(\sin 6x + \sin 4x + \sin 2x).$

Khi đó: $F(x) = \frac{1}{4}\int {(\sin 6x + \sin 4x + \sin 2x)} dx$ $= \frac{1}{4}\left( { – \frac{1}{6}\cos 6x – \frac{1}{4}\cos 4x – \frac{1}{2}\cos 2x} \right) + C$ $= – \frac{1}{{24}}\cos 6x – \frac{1}{{16}}\cos 4x – \frac{1}{4}\cos 2x + C.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-2.html -->
## Ví dụ 13: Tìm họ nguyên hàm của hàm số: $f(x) = \tan x.\tan \left( {\frac{\pi }{3} – x} \right).\tan \left( {\frac{\pi }{3} + x} \right).$

Ta có: $f(x) = \frac{{\sin x.\sin \left( {\frac{\pi }{3} – x} \right).\sin \left( {\frac{\pi }{3} + x} \right)}}{{\cos x.\cos \left( {\frac{\pi }{3} – x} \right).\cos \left( {\frac{\pi }{3} + x} \right)}}.$

Sử dụng các phép biến đổi tích thành tổng, ta được:

$\sin x.\sin \left( {\frac{\pi }{3} – x} \right).\sin \left( {\frac{\pi }{3} + x} \right)$ $= \frac{1}{2}\sin x\left( {\cos 2x – \cos \frac{{2\pi }}{3}} \right)$ $= \frac{1}{2}\cos 2x.\sin x + \frac{1}{4}\sin x$ $= \frac{1}{4}(\sin 3x – \sin x) + \frac{1}{4}\sin x$ $= \frac{1}{4}\sin 3x.$

$\cos x.\cos \left( {\frac{\pi }{3} – x} \right).\cos \left( {\frac{\pi }{3} + x} \right)$ $= \frac{1}{2}\cos x\left( {\cos \frac{{2\pi }}{3} + \cos 2x} \right)$ $= – \frac{1}{4}\cos x + \frac{1}{2}\cos 2x.\cos x$ $= – \frac{1}{4}\cos x + \frac{1}{4}(\cos 3x + \cos x)$ $= \frac{1}{4}\cos 3x.$

Suy ra: $f(x) = \tan 3x.$

Khi đó: $F(x) = \frac{1}{4}\int {\tan } 3xdx$ $= \frac{1}{4}\int {\frac{{\sin 3x}}{{\cos 3x}}} dx =$ $– \frac{1}{{12}}\int {\frac{{d(\cos 3x)}}{{\cos 3x}}}$ $= – \frac{1}{{12}}\ln |\cos 3x| + C.$

<!-- chunk:5 level:2 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-2.html -->
## Dạng 2: Sử dụng công thức hạ bậc.
Cách giải: Ở đây chúng ta ghi nhớ lại các công thức lượng giác:

${\sin ^2}x = \frac{{1 – \cos 2x}}{2}.$

${\cos ^2}x = \frac{{1 + \cos 2x}}{2}.$

${\sin ^3}x = \frac{{3\sin x – \sin 3x}}{4}.$

${\cos ^3}x = \frac{{3\cos x + \cos 3x}}{4}.$

Các công thức trên được sử dụng trong các phép hạ bậc mang tính cục bộ, còn hằng đẳng thức: ${\sin ^2}x + {\cos ^2}x = 1$ được sử dụng trong các phép hạ bậc mang tính toàn cục cho các biểu thức, ví dụ như:

${\sin ^4}x + {\cos ^4}x$ $= {\left( {{{\sin }^2}x + {{\cos }^2}x} \right)^2} – 2{\sin ^2}x.{\cos ^2}x$ $= 1 – \frac{1}{2}{\sin ^2}2x$ $= 1 – \frac{1}{4}(1 – \cos 4x)$ $= \frac{1}{4}\cos 4x + \frac{3}{4}.$

${\sin ^6}x + {\cos ^6}x$ $= {\left( {{{\sin }^2}x + {{\cos }^2}x} \right)^3}$ $– 3{\sin ^2}x.{\cos ^2}x\left( {{{\sin }^2}x + {{\cos }^2}x} \right)$ $= 1 – \frac{3}{4}{\sin ^2}2x$ $= 1 – \frac{3}{8}(1 – \cos 4x)$ $= \frac{3}{8}\cos 4x + \frac{5}{8}.$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-2.html -->
## Ví dụ 14: Tìm họ nguyên hàm của hàm số: $f(x) = {\sin ^4}2x.$

Biến đổi $f(x)$ về dạng: $f(x) = {\left( {\frac{{1 – \cos 4x}}{2}} \right)^2}$ $= \frac{1}{4}\left( {1 – 2\cos 4x + {{\cos }^2}4x} \right)$ $= \frac{1}{4}\left[ {1 – 2\cos 4x + \frac{1}{2}(1 + \cos 8x)} \right]$ $= \frac{1}{8}(3 – 4\cos 4x + \cos 8x).$

Khi đó: $F(x) = \frac{1}{8}\int {\left( {3 – 4\cos 4x + \cos 8x} \right)dx}$ $= \frac{1}{8}\left( {3x – \sin 4x + \frac{1}{8}\sin 8x} \right) + {\rm{C}}{\rm{.}}$

<!-- chunk:7 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-2.html -->
## Ví dụ 15: Tìm họ nguyên hàm của hàm số: $f(x) = {\sin ^8}x + {\cos ^8}x.$

Biến đổi $f(x)$ về dạng: $f(x) = {\left( {{{\sin }^4}x + {{\cos }^4}x} \right)^2} – 2{\sin ^4}x.{\cos ^4}x$ $= {\left( {\frac{1}{4}\cos 4x + \frac{3}{4}} \right)^2} – \frac{1}{8}{\sin ^4}2x$ $= \frac{1}{{16}}{\cos ^2}4x + \frac{3}{8}\cos 4x$ $+ \frac{9}{{16}} – \frac{1}{8}{\left( {\frac{{1 – \cos 4x}}{2}} \right)^2}$ $= \frac{1}{{16}} \cdot \frac{{1 + \cos 8x}}{2} + \frac{3}{8}\cos 4x$ $+ \frac{9}{{16}} – \frac{1}{{32}}{\left( {1 – 2\cos 4x + {{\cos }^2}4x} \right)^2}$ $= \frac{{1 + \cos 8x}}{{32}} + \frac{3}{8}\cos 4x + \frac{9}{{16}}$ $– \frac{1}{{32}}{\left( {1 – 2\cos 4x + \frac{{1 + \cos 8x}}{2}} \right)^2}$ $= \frac{1}{{64}}\cos 8x + \frac{7}{{16}}\cos 4x + \frac{{35}}{{64}}.$

Khi đó: $F\left( x \right) = \frac{1}{{64}}\int {\cos 8xdx} + \frac{7}{{16}}\int {\cos 4xdx} + \frac{{35}}{{64}}\int {dx}$ $= \frac{1}{{512}}\sin 8x + \frac{7}{{64}}\sin 4x + \frac{{35}}{{64}} + C.$

**Chú ý**: Nhiều bài toán cần vận dụng đồng thời hai kỹ thuật biến đổi tổng thành tích và hạ bậc.

<!-- chunk:8 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-2.html -->
## Ví dụ 16: Tìm họ nguyên hàm của hàm số:

a) $f(x) = {\sin ^3}x.\sin 3x.$

b) $f(x) = {\sin ^3}x.\cos 3x + {\cos ^3}x.\sin 3x.$

a) Biến đổi $f(x)$ về dạng: $f(x) = \frac{{3\sin x – \sin 3x}}{4}\sin 3x$ $= \frac{3}{4}\sin 3x.\sin x – \frac{1}{4}{\sin ^2}3x$ $= \frac{3}{8}\left( {\cos 2x – \cos 4x} \right) – \frac{1}{8}\left( {1 – \cos 6x} \right)$ $= \frac{1}{8}\left( {3\cos 2x – 3\cos 4x + \cos 6x – 1} \right).$

Khi đó: $F(x) = \frac{1}{8}\int {(3\cos 2x – 3\cos 4x + \cos 6x – 1)} dx$ $= \frac{1}{8}\left( {\frac{3}{2}\sin 2x – \frac{3}{4}\sin 4x + \frac{1}{6}\sin 6x – x} \right) + C.$

b. Biến đổi $f(x)$ về dạng: $f(x) = \frac{{3\sin x – \sin 3x}}{4}\cos 3x$ $+ \frac{{\cos 3x + 3\cos x}}{4}\sin 3x$ $= \frac{3}{4}(\cos 3x.\sin x + \sin 3x.\cos x)$ $= \frac{3}{4}\sin 4x.$

Khi đó: $F\left( x \right) = \frac{3}{4}\int {\sin 4xdx}$ $= – \frac{3}{{16}}\cos 4x + C.$

**Dạng 3: Sử dụng các phép biến đổi lượng giác khác nhau.

Cách giải**: Ở đây ngoài việc vận dụng một cách linh hoạt các công thức biến đổi lượng giác các em học sinh còn cần thiết biết cách định hướng trong phép biến đổi.

<!-- chunk:9 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-2.html -->
## Ví dụ 17: Tìm họ nguyên hàm của hàm số:

a) $f(x) = \frac{{\sin x – \cos x}}{{\sin x + \cos x}}.$

b) $f(x) = \frac{{\cos 2x}}{{\sin x + \cos x}}.$

a) Ta có: $F(x) = \int {\frac{{\sin x – \cos x}}{{\sin x + \cos x}}} dx$ $= – \int {\frac{{d(\sin x + \cos x)}}{{\sin x + \cos x}}}$ $= – \ln (\sin x + \cos x) + C.$

b) Ta có: $F(x) = \int {\frac{{\cos 2x}}{{\sin x + \cos x}}} dx$ $= \int {\frac{{{{\cos }^2}x – {{\sin }^2}x}}{{\sin x + \cos x}}} dx$ $= \int {(\cos x – \sin x)} dx$ $= \sin x + \cos x + C.$

<!-- chunk:10 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-2.html -->
## Ví dụ 18: Tìm nguyên hàm: $I = \int {\frac{{\sin 3x.\sin 4x}}{{\tan x + \cot 2x}}} dx.$

Biến đổi biểu thức dưới dấu tích phân về dạng: $\frac{{\sin 3x.\sin 4x}}{{\tan x + \cot 2x}}$ $= \frac{{\sin 3x.\sin 4x}}{{\frac{{\cos x}}{{\cos x.\sin 2x}}}}$ $= \sin 4x.\sin 3x.\sin 2x$ $= \frac{1}{2}(\cos x – \cos 7x)\sin 2x$ $= \frac{1}{2}(\sin 2x.\cos x – \cos 7x.\sin 2x)$ $= \frac{1}{4}(\sin 3x + \sin x – \sin 9x + \sin 5x).$

Khi đó: $I = \frac{1}{4}\int {(\sin x + \sin 3x + \sin 5x – \sin 9x)} dx$ $= – \frac{1}{4}\left( {\cos x + \frac{1}{3}\cos 3x + \frac{1}{5}\cos 5x – \frac{1}{9}\cos 9x} \right) + C.$

Tổng quát: Các nguyên hàm dạng $\int {{{\sin }^m}} x.{\cos ^n}xdx$ với $m$, $n$ là những số nguyên được tính nhờ các phép biến đổi hoặc dùng công thức hạ bậc.

Phương pháp 3: Tính tích phân các hàm lượng giác bằng phương pháp đổi biến.
Phương pháp chung: Để tìm nguyên hàm dạng $I = \int {\rm{R}} (\sin x,\cos x)dx$, trong đó $R$ là hàm hữu tỉ, ta lựa chọn một trong các hướng giải sau:

+ Hướng 1: Nếu ${\rm{R}}( – \sin x,\cos x) = – {\rm{R}}(\sin x,\cos x)$ thì sử dụng phép đổi biến tương ứng là: $t = \cos x.$

+ Hướng 2: Nếu $R(\sin x, – \cos x) = – R(\sin x,\cos x)$ thì sử dụng phép đổi biến tương ứng là: $t = \sin x.$

+ Hướng 3: Nếu ${\rm{R}}( – \sin x, – \cos x) = R (\sin x,\cos x)$ thì sử dụng phép đổi biến: $t = \tan x$ (một số trường hợp có thể là: $t = cot x$).

Do đó với các nguyên hàm dạng:

Nguyên hàm $I = \int {{{\tan }^n}} xdx$, với $n∈Z$ được xác định nhờ phép đổi biến: $t = \tan x.$

Nguyên hàm $I = \int {co{t^n}} xdx$, với $n∈Z$ được xác định nhờ phép đổi biến $t = \cot x.$

+ Hướng 4: Mọi trường hợp đều có thể đưa về tích phân các hàm hữu tỉ bằng phép đổi biến $t = \tan \frac{x}{2}.$

<!-- chunk:11 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-2.html -->
## Ví dụ 19: Tìm nguyên hàm: $I = \int {\frac{{\cos x + \sin x.\cos x}}{{2 + \sin x}}} dx.$

Biến đổi $I$ về dạng: $I = \int {\frac{{(1 + \sin x)\cos x}}{{2 + \sin x}}} dx.$

Đặt $t = \sin x$ suy ra: $dt = \cos xdx$ và $\frac{{(1 + \sin x)\cos x}}{{2 + \sin x}}dx = \frac{{1 + t}}{{2 + t}}dt.$

Khi đó: $I = \int {\frac{{1 + t}}{{2 + t}}} dt$ $= \int {\left( {1 – \frac{1}{{2 + t}}} \right)} dt$ $= t – \ln |2 + t| + C$ $= \sin x – \ln |2 + \sin x| + C.$

Nhận xét: Trong bài toán trên sở dĩ ta định hướng được phép biến đổi như vậy là bởi nhận xét rằng: $R(\sin x, – \cos x) = – R(\sin x,\cos x)$, do đó sử dụng phép đổi biến tương ứng là $t = \sin x.$

<!-- chunk:12 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-2.html -->
## Ví dụ 20: Tìm nguyên hàm: $I = \int {\frac{{dx}}{{\sin x.{{\cos }^3}x}}} .$

Biến đổi $I$ về dạng: $I = \int {\frac{{dx}}{{\tan x.{{\cos }^4}x}}} .$

Đặt $t = \tan x$, suy ra: $dt = \frac{{dx}}{{{{\cos }^2}x}}$ và $\frac{{dx}}{{\tan x.{{\cos }^4}x}}$ $= \frac{1}{{\tan x}}\left( {1 + {{\tan }^2}x} \right)\frac{{dx}}{{{{\cos }^2}x}}$ $= \frac{{\left( {1 + {t^2}} \right)dt}}{t}$ $= \left( {\frac{1}{t} + t} \right)dt.$

Khi đó: $I = \int {\left( {\frac{1}{t} + t} \right)dt}$ $= \ln |t| + \frac{1}{2}{t^2} + C$ $= \ln \left| {\tan x} \right| + \frac{1}{2}{\tan ^2}x + C.$

Nhận xét:

+ Trong bài toán trên sở dĩ ta định hướng được phép biến đổi như vậy là bởi nhận xét rằng: $R( – \sin x, – \cos x) = R(\sin x,\cos x).$

+ Việc đánh giá hàm số dưới dấu tích phân như trên để lựa chọn phép đặt ẩn phụ thích hợp luôn tỏ ra rất hiệu quả đối với bài toán xác định nguyên hàm của các hàm lượng giác chứa căn. Ta đi xem xét ví dụ sau:

<!-- chunk:13 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-2.html -->
## Ví dụ 21: Tìm nguyên hàm: $I = \int {\frac{{dx}}{{\sqrt[4]{{{{\sin }^3}x.{{\cos }^5}x}}}}} .$

Biến đổi $I$ về dạng: $I = \int {\frac{{dx}}{{\sqrt[4]{{{{\tan }^3}x.{{\cos }^8}x}}}}}$ $= \int {\frac{{dx}}{{{{\cos }^2}x.\sqrt[4]{{{{\tan }^3}x}}}}.}$

Đặt $t = \tan x$, suy ra: $dt = \frac{{dx}}{{{{\cos }^2}x}}$ và $\frac{{dx}}{{{{\cos }^2}x.\sqrt[4]{{{{\tan }^3}x}}}} = \frac{{dt}}{{\sqrt[4]{{{t^3}}}}}.$

Khi đó: $I = \int {\frac{{dt}}{{\sqrt[4]{{{t^3}}}}}}$ $= 4\sqrt[4]{t} + C$ $= 4\sqrt[4]{{\tan x}} + C.$

<!-- chunk:14 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-2.html -->
## Ví dụ 22: Tìm nguyên hàm: $I = \int {\frac{{\sin xdx}}{{\cos x\sqrt {{{\sin }^2}x + 1} }}} .$

Đặt $t = \cos x \Rightarrow dt = – \sin xdx$, do đó: $I = – \int {\frac{{dt}}{{t\sqrt {2 – {t^2}} }}} .$

Ta cần xét 2 trường hợp: $t>0$ và $t<0:$

+ Với $t>0$, ta có: $I = – \int {\frac{{dt}}{{{t^2}\sqrt {\frac{2}{{{t^2}}} – 1} }}}$ $= \int {\frac{{d\left( {\frac{1}{t}} \right)}}{{\sqrt {\frac{2}{{{t^2}}} – 1} }}}$ $= \frac{1}{{\sqrt 2 }}\ln \left| {\frac{{\sqrt 2 }}{t} + \sqrt {\frac{2}{{{t^2}}} – 1} } \right| + C$ $= \frac{1}{{\sqrt 2 }}\ln \left| {\frac{{\sqrt 2 + \sqrt {2 – {t^2}} }}{t}} \right| + C.$

+ Với $t<0$, ta có: $I = \int {\frac{{dt}}{{{t^2}\sqrt {\frac{2}{{{t^2}}} – 1} }}}$ $= – \int {\frac{{d\left( {\frac{1}{t}} \right)}}{{\sqrt {\frac{2}{{{t^2}}} – 1} }}}$ $= – \frac{1}{{\sqrt 2 }}\ln \left| {\frac{{\sqrt 2 }}{t} + \sqrt {\frac{2}{{{t^2}}} – 1} } \right| + C$ $= – \frac{1}{{\sqrt 2 }}\ln \left| {\frac{{\sqrt 2 – \sqrt {2 – {t^2}} }}{t}} \right| + C$ $= \frac{1}{{\sqrt 2 }}\ln \left| {\frac{{\sqrt 2 + \sqrt {2 – {t^2}} }}{t}} \right| + C.$

Tóm lại ta được: $I = \frac{1}{{\sqrt 2 }}\ln \left| {\frac{{\sqrt 2 + \sqrt {2 – {t^2}} }}{t}} \right| + C$ $= \frac{1}{{\sqrt 2 }}\ln \left| {\frac{{\sqrt 2 + \sqrt {1 + {{\sin }^2}x} }}{{\cos x}}} \right| + C.$

Phương pháp 4: Xác định nguyên hàm các hàm lượng giác bằng phương pháp tích phân từng phần.
Phương pháp chung:

<!-- chunk:15 level:2 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-2.html -->
## Dạng 1: Tìm nguyên hàm: $\int {P\left( x \right)} \sin \alpha xdx$ hoặc $\int {P\left( x \right)} \cos \alpha xdx$, với $P$ là một đa thức thuộc $R[X]$ và $α∈R^*.$

Khi đó, ta đặt: 
$$
\left\{ {\begin{array}{l}
{u = P(x)}\\
{dv = \sin \alpha xdx}
\end{array}} \right.
$$
 hoặc 
$$
\left\{ {\begin{array}{l}
{u = P(x)}\\
{dv = \cos \alpha xdx}
\end{array}} \right.
$$

<!-- chunk:16 level:2 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-2.html -->
## Dạng 2: Tìm nguyên hàm: $\int {{e^{ax}}\cos bxdx}$ hoặc $\int {{e^{ax}}\sin bxdx}$ với $a,b \ne 0.$

Khi đó, ta đặt: 
$$
\left\{ {\begin{array}{l}
{u = \cos bx}\\
{dv = {e^{ax}}dx}
\end{array}} \right.
$$
 hoặc 
$$
\left\{ {\begin{array}{l}
{u = \sin bx}\\
{dv = {e^{ax}}dx}
\end{array}} \right.
$$

<!-- chunk:17 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-2.html -->
## Ví dụ 23: Tìm nguyên hàm: $I = \int {\frac{x}{{{{\cos }^2}x}}dx} .$

Sử dụng phương pháp tích phân từng phần, bằng cách đặt: 
$$
\left\{ {\begin{array}{l}
{u = x}\\
{dv = \frac{{dx}}{{{{\cos }^2}x}}}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{du = dx}\\
{v = \tan x}
\end{array}} \right.
$$

Khi đó: $I = x\tan x – \int {\tan } xdx$ $= x\tan x – \int {\frac{{\sin x}}{{\cos x}}} dx$ $= x\tan x + \int {\frac{{d(\cos x)}}{{\cos x}}}$ $= x\tan x + \ln |\cos x| + C.$

<!-- chunk:18 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-2.html -->
## Ví dụ 24: Tìm nguyên hàm: $I = \int {\frac{{{{\cos }^2}xdx}}{{{{\sin }^3}x}}} .$

Biến đổi $I$ về dạng: $I = \int {\frac{{\cos x \cdot d(\sin x)}}{{{{\sin }^3}x}}} .$

Đặt 
$$
\left\{ {\begin{array}{l}
{u = \cos x}\\
{dv = \frac{{d(\sin x)}}{{{{\sin }^3}x}}}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{du = – \sin xdx}\\
{v = – \frac{1}{{{{\sin }^2}x}}}
\end{array}} \right.
$$

Khi đó: $I = – \frac{{\cos x}}{{{{\sin }^2}x}} – \int {\frac{{dx}}{{\sin x}}}$ $= – \frac{{\cos x}}{{{{\sin }^2}x}} – \int d \left( {\ln \left| {\tan \frac{x}{2}} \right|} \right)$ $= – \frac{{\cos x}}{{{{\sin }^2}x}} – \ln \left| {\tan \frac{x}{2}} \right| + C.$

Chú ý: Bài toán trên cũng có thể giải được bằng phương pháp đổi biến số, bằng cách nhận xét rằng: ${\rm{R}}( – \sin x,\cos x) = – {\rm{R}}(\sin x,\cos x)$, ta sử dụng phép đổi biến tương ứng là $t=\cos x.$