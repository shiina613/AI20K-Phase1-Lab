# Loại nghiệm không thích hợp khi giải phương trình lượng giác

<!-- chunk:0 level:0 source:https://toanmath.com/2019/08/loai-nghiem-khong-thich-hop-khi-giai-phuong-trinh-luong-giac.html -->
Bài viết hướng dẫn phương pháp loại bỏ các nghiệm không thích hợp (không thỏa mãn điều kiện, không thỏa mãn yêu cầu bài toán) khi giải phương trình lượng giác.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/08/loai-nghiem-khong-thich-hop-khi-giai-phuong-trinh-luong-giac.html -->
## I. PHƯƠNG PHÁP
Bài toán: Loại nghiệm không thích hợp của phương trình lượng giác.

PHƯƠNG PHÁP CHUNG:

Ta thường gặp hai dạng toán sau:

<!-- chunk:2 level:2 source:https://toanmath.com/2019/08/loai-nghiem-khong-thich-hop-khi-giai-phuong-trinh-luong-giac.html -->
## Dạng 1: Tìm nghiệm thuộc $(a,b)$ của phương trình.

Ta thực hiện theo các bước:

+ Bước 1: Đặt điều kiện có nghĩa cho phương trình.

+ Bước 2: Giải phương trình để tìm nghiệm $x = \alpha + \frac{{2k\pi }}{n}$, $k,n \in Z.$

+ Bước 3: Tìm nghiệm thuộc $(a,b):$

$a < \alpha + \frac{{2k\pi }}{n} < b$ $\mathop \Leftrightarrow \limits^{k,n \in Z} \left( {{k_0},{n_0}} \right)$ $\Rightarrow {x_0} = \alpha + \frac{{2{k_0}\pi }}{{{n_0}}}.$

<!-- chunk:3 level:2 source:https://toanmath.com/2019/08/loai-nghiem-khong-thich-hop-khi-giai-phuong-trinh-luong-giac.html -->
## Dạng 2: Phương trình chứa ẩn ở mẫu.

Ta thực hiện theo các bước:

+ Bước 1: Đặt điều kiện có nghĩa cho phương trình $x \ne \beta + \frac{{2l\pi }}{n}$, $l,n \in Z.$

+ Bước 2: Giải phương trình để tìm nghiệm ${x_0} = \alpha + \frac{{2k\pi }}{n}$, $k,n \in Z.$

+ Bước 3: Kiểm tra điều kiện ta lựa chọn một trong hai phương pháp sau:

Phương pháp đại số:

Nghiệm ${x_0}$ bị loại khi và chỉ khi:

$\alpha + \frac{{2k\pi }}{n} = \beta + \frac{{2l\pi }}{n}.$

Nghiệm ${x_0}$ chấp nhận được khi và chỉ khi:

$\alpha + \frac{{2k\pi }}{n} \ne \beta + \frac{{2l\pi }}{n}.$

Phương pháp hình học:

Biểu diễn các điểm $x = \beta + \frac{{2l\pi }}{n}$, $l,n \in Z$ trên đường tròn đơn vị, khi đó ta được tập các điểm $C = \left\{ {{C_1}, \ldots ,{C_p}} \right\}.$

Biểu diễn các điểm $x = \alpha + \frac{{2k\pi }}{n}$, $k,n \in Z$ trên đường tròn đơn vị, khi đó ta được tập các điểm $D = \left\{ {{D_1}, \ldots ,{D_q}} \right\}.$

Lấy tập $E = D\backslash C = \left\{ {{E_1}, \ldots ,{E_r}} \right\}$, từ đó kết luận nghiệm của phương trình là:

$x = {E_1} + 2k\pi$, …, $x = {E_r} + 2k\pi$, $k \in Z.$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/08/loai-nghiem-khong-thich-hop-khi-giai-phuong-trinh-luong-giac.html -->
## Ví dụ 1: Tìm các nghiệm thuộc $\left( {\frac{\pi }{2},3\pi } \right)$ của phương trình:

$\sin \left( {2x + \frac{{5\pi }}{2}} \right) – 3\cos \left( {x – \frac{{7\pi }}{2}} \right)$ $= 1 + 2\sin x.$

Biến đổi phương trình về dạng:

$\sin \left( {2x + \frac{\pi }{2} + 2\pi } \right)$ $– 3\cos \left( {x + \frac{\pi }{2} – 4\pi } \right)$ $= 1 + 2\sin x.$

$\Leftrightarrow \cos 2x + 3\sin x = 1 + 2\sin x$ $\Leftrightarrow 1 – 2{\sin ^2}x = 1 – \sin x$ $\Leftrightarrow 2{\sin ^2}x – \sin x = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\sin x = 0}\\
{\sin x = \frac{1}{2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = k\pi }\\
{x = \frac{\pi }{6} + 2k\pi }\\
{x = \frac{{5\pi }}{6} + 2k\pi }
\end{array}} \right.
$$
 
$$
\mathop \Leftrightarrow \limits^{x \in \left( {\frac{\pi }{2},3\pi } \right)} \left[ {\begin{array}{l}
{x = \pi ,x = 2\pi }\\
{x = \frac{{13\pi }}{6}}\\
{x = \frac{{5\pi }}{6},x = \frac{{17\pi }}{6}}
\end{array}} \right..
$$

Vậy phương trình có $5$ nghiệm.

<!-- chunk:5 level:3 source:https://toanmath.com/2019/08/loai-nghiem-khong-thich-hop-khi-giai-phuong-trinh-luong-giac.html -->
## Ví dụ 2: Tìm các nghiệm thuộc $[0,2\pi ]$ của phương trình:

$5\left( {\sin x + \frac{{\cos 3x + \sin 3x}}{{1 + 2\sin 2x}}} \right)$ $= \cos 2x + 3.$

Điều kiện:

$1 + 2\sin 2x \ne 0$ $\Leftrightarrow \sin 2x \ne – \frac{1}{2}$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{2x \ne – \frac{\pi }{6} + 2k\pi }\\
{2x \ne \frac{{7\pi }}{6} + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x \ne – \frac{\pi }{{12}} + k\pi }\\
{x \ne \frac{{7\pi }}{{12}} + k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Ta có:

$\cos 3x + \sin 3x$ $= 4{\cos ^3}x – 3\cos x + 3\sin x – 4{\sin ^3}x.$

$= 4\left( {{{\cos }^3}x – {{\sin }^3}x} \right) – 3(\cos x – \sin x).$

$= (\cos x – \sin x)[4(1 + \cos x\sin x) – 3]$ $= (\cos x – \sin x)(1 + 2\sin 2x).$

Khi đó phương trình có dạng:

$5(\sin x + \cos x – \sin x) = \cos 2x + 3$ $\Leftrightarrow 2{\cos ^2}x – 5\cos x + 2 = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\cos x = 2\:{\rm{(loại)}}}\\
{\cos x = \frac{1}{2}}
\end{array}} \right.
$$
 $\Leftrightarrow x = \pm \frac{\pi }{3} + 2k\pi$, $k \in Z$ 
$$
\mathop \Leftrightarrow \limits^{x \in \left[ {0,2\pi } \right]} \left[ {\begin{array}{l}
{x = \frac{\pi }{3}}\\
{x = \frac{{5\pi }}{3}}
\end{array}} \right..
$$

Vậy phương trình có hai nghiệm.

<!-- chunk:6 level:3 source:https://toanmath.com/2019/08/loai-nghiem-khong-thich-hop-khi-giai-phuong-trinh-luong-giac.html -->
## Ví dụ 3: Giải phương trình:

$\frac{1}{{\cos x}} + \frac{1}{{\sin 2x}} = \frac{2}{{\sin 4x}}.$

Điều kiện:

$\sin 4x \ne 0 \Leftrightarrow x \ne \frac{{k\pi }}{4}$, $k \in Z$ $(*).$

Biến đổi phương trình về dạng:

$4\sin x\cos 2x + 2\cos 2x = 2$ $\Leftrightarrow 2\sin x\cos 2x = 1 – \cos 2x.$

$\Leftrightarrow 2\sin x\cos 2x = 2{\sin ^2}x$ $\Leftrightarrow (\cos 2x – \sin x)\sin x = 0.$

$\Leftrightarrow \left( {1 – 2{{\sin }^2}x – \sin x} \right)\sin x = 0$ $\Leftrightarrow (\sin x + 1)(2\sin x – 1)\sin x = 0.$

$\mathop \Leftrightarrow \limits^{(*)} \sin x = \frac{1}{2}$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \frac{\pi }{6} + 2k\pi }\\
{x = \frac{{5\pi }}{6} + 2k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

Nhận xét: Trong lời giải trên chúng ta đã linh hoạt trong việc kiểm tra điều kiện $(*)$ để loại đi các nghiệm $\sin x = 0$ và $\sin x = – 1$ bởi:

$\sin 4x = 4\sin x\cos x\cos 2x.$

<!-- chunk:7 level:3 source:https://toanmath.com/2019/08/loai-nghiem-khong-thich-hop-khi-giai-phuong-trinh-luong-giac.html -->
## Ví dụ 4: Giải phương trình:

$\frac{{\sin x\cot 5x}}{{\cos 9x}} = 1.$

Điều kiện:

$$
\left\{ {\begin{array}{l}
{\sin 5x \ne 0}\\
{\cos 9x \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{5x \ne l\pi }\\
{9x \ne \frac{\pi }{2} + l\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ne \frac{{l\pi }}{5}}\\
{x \ne \frac{\pi }{{18}} + \frac{{l\pi }}{9}}
\end{array}} \right.
$$
, $l \in Z$ $(*).$

Biến đổi phương trình về dạng:

$\cos 5x\sin x = \cos 9x\sin 5x$ $\Leftrightarrow \frac{1}{2}(\sin 6x – \sin 4x)$ $= \frac{1}{2}(\sin 14x – \sin 4x).$

$\Leftrightarrow \sin 14x = \sin 6x$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{14x = 6x + 2k\pi }\\
{14x = \pi – 6x + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \frac{{k\pi }}{4}}\\
{x = \frac{\pi }{{20}} + \frac{{k\pi }}{{10}}}
\end{array}} \right.
$$
, $k \in Z.$

Kiểm tra điều kiện $(*):$

+ Với $x = \frac{{k\pi }}{4}$, ta cần có:

$$
\left\{ {\begin{array}{l}
{\frac{{k\pi }}{4} \ne \frac{{l\pi }}{5}}\\
{\frac{{k\pi }}{4} \ne \frac{\pi }{{18}} + \frac{{l\pi }}{9}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{5k \ne 4l}\\
{9k \ne 2 + 4l}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{k = 4n + 1}\\
{k = 4n + 3}
\end{array}} \right.
$$
 
$$
\Rightarrow \left[ {\begin{array}{l}
{x = \frac{{(4n + 1)\pi }}{4}}\\
{x = \frac{{(4n + 3)\pi }}{4}}
\end{array}} \right.
$$
, $n \in Z.$

+ Với $x = \frac{\pi }{{20}} + \frac{{k\pi }}{{10}}$, ta cần có:

$$
\left\{ {\begin{array}{l}
{\frac{\pi }{{20}} + \frac{{k\pi }}{{10}} \ne \frac{{l\pi }}{5}}\\
{\frac{\pi }{{20}} + \frac{{k\pi }}{{10}} \ne \frac{\pi }{{18}} + \frac{{l\pi }}{9}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{1 + 2k \ne 4l}\\
{18k \ne 1 + 20l}
\end{array}} \right.
$$
 luôn đúng $\Rightarrow x = \frac{\pi }{{20}} + \frac{{k\pi }}{{10}}$, $k \in Z.$

Vậy phương trình có ba họ nghiệm.

Nhận xét: Trong lời giải trên từ:

$$
\left\{ {\begin{array}{l}
{5k \ne 4l\:(1)}\\
{9k \ne 2 + 4l\:(2)}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{k = 4n + 1}\\
{k = 4n + 3}
\end{array}} \right..
$$

Bởi từ $(1)$ suy ra $k$ không chia hết cho $4$ và từ $(2)$ suy ra $k$ lẻ, do đó:

$$
\left[ {\begin{array}{l}
{k = 4n + 1}\\
{k = 4n + 3}
\end{array}} \right.
$$
 $(I).$

Rồi lại thực hiện phép thử $(I)$ và $(2).$

Còn đối với:

$$
\left\{ {\begin{array}{l}
{1 + 2k \ne 4l}\\
{18k \ne 1 + 20l}
\end{array}} \right.
$$
 luôn đúng.

Xuất phát từ tính chẵn lẻ của hai vế.

<!-- chunk:8 level:3 source:https://toanmath.com/2019/08/loai-nghiem-khong-thich-hop-khi-giai-phuong-trinh-luong-giac.html -->
## Ví dụ 5: Giải phương trình:

$\sin 3x = \cos x\cos 2x\left( {{{\tan }^2}x + \tan 2x} \right).$

Điều kiện:

$$
\left\{ {\begin{array}{l}
{\cos x \ne 0}\\
{\cos 2x \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ne \frac{\pi }{2} + k\pi }\\
{2x \ne \frac{\pi }{2} + k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ne \frac{\pi }{2} + k\pi }\\
{x \ne \frac{\pi }{4} + \frac{{k\pi }}{2}}
\end{array}} \right.
$$
, $k \in Z.$ $(*).$

Biến đổi phương trình về dạng:

$\sin 3x = \cos x\cos 2x\left( {\frac{{{{\sin }^2}x}}{{{{\cos }^2}x}} + \frac{{\sin 2x}}{{\cos 2x}}} \right)$ $\Leftrightarrow \sin 3x = \frac{{{{\sin }^2}x\cos 2x}}{{\cos x}} + \sin 2x\cos x.$

$\Leftrightarrow \left( {3\sin x – 4{{\sin }^3}x} \right)\cos x$ $= \left( {\cos 2x\sin x + 2{{\cos }^3}x} \right)\sin x.$

$\Leftrightarrow \left[ {\left( {3 – 4{{\sin }^2}x} \right)\cos x – \left( {\cos 2x\sin x + 2{{\cos }^3}x} \right)} \right]\sin x = 0.$

$\Leftrightarrow (\cos x – \sin x)\cos 2x\sin x = 0$ $\mathop \Leftrightarrow \limits^{\left( * \right)} \sin x = 0$ $\Leftrightarrow x = k\pi$, $k \in Z.$

Vậy phương trình có một họ nghiệm.

<!-- chunk:9 level:1 source:https://toanmath.com/2019/08/loai-nghiem-khong-thich-hop-khi-giai-phuong-trinh-luong-giac.html -->
## II. CÁC BÀI TOÁN THI

## Bài 1: Tìm $x$ thuộc đoạn $[0,14]$ là nghiệm đúng nghiệm phương trình:

$\cos 3x – 4\cos 2x + 3\cos x – 4 = 0.$

Biến đổi phương trình về dạng:

$4{\cos ^3}x – 3\cos x$ $– 4(\cos 2x + 1) + 3\cos x = 0.$

$\Leftrightarrow 4{\cos ^3}x – 8{\cos ^2}x = 0$ $\Leftrightarrow \cos x = 0$ $\Leftrightarrow x = \frac{\pi }{2} + k\pi$, $k \in Z.$

Vì $x \in [0,14]$ nên:

$0 \le \frac{\pi }{2} + k\pi \le 14$ $\Leftrightarrow – \frac{1}{2} \le k \le \frac{{14 – \frac{\pi }{2}}}{\pi }$ $\Leftrightarrow k = 0,1,2,3.$

Vậy phương trình có các nghiệm $x = \frac{\pi }{2}$, $x = \frac{{3\pi }}{2}$, $x = \frac{{5\pi }}{2}$, $x = \frac{{7\pi }}{2}.$

## Bài 2: Giải phương trình:

$\frac{{\cos 2x + 3\cot 2x + \sin 4x}}{{\cot 2x – \cos 2x}} = 2.$

Điều kiện:

$$
\left\{ {\begin{array}{l}
{\sin 2x \ne 0}\\
{\cot 2x – \cos 2x \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\sin 2x \ne 0}\\
{\left( {\frac{1}{{\sin 2x}} – 1} \right)\cos 2x \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\sin 2x \ne 0}\\
{\cos 2x \ne 0}\\
{\sin 2x \ne 1}
\end{array}} \right..
$$

$\Leftrightarrow \sin 4x \ne 0$ $\Leftrightarrow x \ne \frac{{k\pi }}{4}$ $k \in Z.$

Biến đổi phương trình về dạng:

$\cos 2x + 3\frac{{\cos 2x}}{{\sin 2x}} + 2\sin 2x\cos 2x$ $= 2\left( {\frac{{\cos 2x}}{{\sin 2x}} – \cos 2x} \right).$

$\Leftrightarrow 1 + \frac{3}{{\sin 2x}} + 2\sin 2x$ $= 2\left( {\frac{1}{{\sin 2x}} – 1} \right)$ $\Leftrightarrow 2{\sin ^2}2x + 3\sin 2x + 1 = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\sin 2x = – 1\:{\rm{(loại)}}}\\
{\sin 2x = – \frac{1}{2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{2x = – \frac{\pi }{6} + 2k\pi }\\
{2x = \pi + \frac{\pi }{6} + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – \frac{\pi }{{12}} + k\pi }\\
{x = \frac{{7\pi }}{{12}} + k\pi }
\end{array}} \right.
$$
, $k \in Z.$

## Bài 3: Giải phương trình:

$\frac{{{{(1 – \cos x)}^2} + {{(1 + \cos x)}^2}}}{{4(1 – \sin x)}}$ $– {\tan ^2}x\sin x$ $= \frac{{1 + \sin x}}{2} + {\tan ^2}x.$

Điều kiện:

$$
\left\{ {\begin{array}{l}
{\sin x \ne 1}\\
{\cos x \ne 0}
\end{array}} \right.
$$
 $\Leftrightarrow \cos x \ne 0$ $\Leftrightarrow x \ne \frac{\pi }{2} + k\pi$, $k \in Z.$

Biến đổi phương trình về dạng:

$\frac{{2 + 2{{\cos }^2}x}}{{4(1 – \sin x)}}$ $= \frac{{1 + \sin x}}{2} + (1 + \sin x){\tan ^2}x.$

$\Leftrightarrow \frac{{1 + {{\cos }^2}x}}{{2(1 – \sin x)}}$ $= \frac{{1 + \sin x}}{2}\left( {1 + 2{{\tan }^2}x} \right)$ $= \frac{{1 + \sin x}}{2}.\frac{{{{\cos }^2}x + 2{{\sin }^2}x}}{{{{\cos }^2}x}}$ $= \frac{{1 + \sin x}}{2}.\frac{{{{\cos }^2}x + 2{{\sin }^2}x}}{{1 – {{\sin }^2}x}}$ $= \frac{{{{\cos }^2}x + 2{{\sin }^2}x}}{{2(1 – \sin x)}}.$

$\Leftrightarrow 1 + {\cos ^2}x = {\cos ^2}x + 2{\sin ^2}x$ $\Leftrightarrow 1 – 2{\sin ^2}x = 0.$

$\Leftrightarrow \cos 2x = 0$ $\Leftrightarrow x = \frac{\pi }{4} + \frac{{k\pi }}{2}$, $k \in Z.$

Vậy phương trình có một họ nghiệm: $x = \frac{\pi }{4} + \frac{{k\pi }}{2}$, $k \in Z.$

## Bài 4: Giải phương trình:

$3{\sin ^2}x + \frac{1}{2}\sin 2x + 2{\cos ^2}x$ $= \frac{{3\left( {{{\sin }^4}x + {{\cos }^4}x – 1} \right)}}{{{{\sin }^6}x + {{\cos }^6}x – 1}}.$

Ta có:

${\sin ^4}x + {\cos ^4}x – 1$ $= {\left( {{{\sin }^2}x + {{\cos }^2}x} \right)^2} – 2{\sin ^2}x{\cos ^2}x – 1$ $= – 2{\sin ^2}x{\cos ^2}x.$

${\sin ^6}x + {\cos ^6}x – 1$ $= {\left( {{{\sin }^2}x + {{\cos }^2}x} \right)^3}$ $– 3{\sin ^2}x{\cos ^2}x\left( {{{\sin }^2}x + {{\cos }^2}x} \right) – 1$ $= – 3{\sin ^2}x{\cos ^2}x.$

Điều kiện:

${\sin ^6}x + {\cos ^6}x – 1 \ne 0$ $\Leftrightarrow – 3{\sin ^2}x{\cos ^2}x \ne 0$ $\Leftrightarrow \sin 2x \ne 0$ $\Leftrightarrow x \ne \frac{{k\pi }}{2}$, $k \in Z$ $(*).$

Biến đổi phương trình về dạng:

$3{\sin ^2}x + \frac{1}{2}\sin 2x + 2{\cos ^2}x = 2$ $\Leftrightarrow {\sin ^2}x + \sin x\cos x = 0.$

$\Leftrightarrow \sin x(\sin x + \cos x) = 0$ $\mathop \Leftrightarrow \limits^{(*)} \sin x + \cos x = 0$ $\Leftrightarrow x = – \frac{\pi }{4} + k\pi$, $k \in Z.$

Vậy phương trình có một họ nghiệm $x = – \frac{\pi }{4} + k\pi$, $k \in Z.$

## Bài 5: Giải phương trình:

$\frac{{{{\sin }^4}2x + {{\cos }^4}2x}}{{\tan \left( {\frac{\pi }{4} – x} \right)\tan \left( {\frac{\pi }{4} + x} \right)}} = {\cos ^4}2x.$

Ta có:

$\tan \left( {\frac{\pi }{4} – x} \right)\tan \left( {\frac{\pi }{4} + x} \right)$ $= \tan \left( {\frac{\pi }{4} – x} \right)\cot \left( {\frac{\pi }{2} – \frac{\pi }{4} – x} \right)$ $= \tan \left( {\frac{\pi }{4} – x} \right)\cot \left( {\frac{\pi }{4} – x} \right) = 1.$

Điều kiện:

$$
\left\{ {\begin{array}{l}
{\cos \left( {\frac{\pi }{4} – x} \right) \ne 0}\\
{\cos \left( {\frac{\pi }{4} + x} \right) \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x – \frac{\pi }{4} \ne \frac{\pi }{2} + k\pi }\\
{\frac{\pi }{4} + x \ne \frac{\pi }{2} + k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ne \frac{{3\pi }}{4} + k\pi }\\
{x \ne \frac{\pi }{4} + k\pi }
\end{array}} \right.
$$
 $\Leftrightarrow x \ne \frac{\pi }{4} + \frac{{k\pi }}{2}$, $k \in Z.$

Biến đổi phương trình về dạng:

${\sin ^4}2x + {\cos ^4}2x = {\cos ^4}2x$ $\Leftrightarrow {\sin ^4}2x = 0$ $\Leftrightarrow \sin 2x = 0$ $\Leftrightarrow x = \frac{{k\pi }}{2}$, $k \in Z.$

Vậy phương trình có một họ nghiệm $x = \frac{{k\pi }}{2}$, $k \in Z.$

## Bài 6: Giải phương trình:

$\frac{{\sin 5x}}{{5\sin x}} = 1.$

Điều kiện:

$\sin x \ne 0$ $\Leftrightarrow x \ne k\pi$, $k \in Z.$

Biến đổi phương trình về dạng:

$\sin 5x = 5\sin x$ $\Leftrightarrow \sin 5x – \sin x = 4\sin x$ $\Leftrightarrow 2\cos 3x\sin 2x = 4\sin x.$

$\Leftrightarrow 4\cos 3x\sin x\cos x = 4\sin x$ $\Leftrightarrow (\cos 3x\cos x – 1)\sin x = 0$ $\Leftrightarrow \cos 3x\cos x = 1.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{\cos x = 1}\\
{\cos 3x = 1}
\end{array}} \right.}\\
{\left\{ {\begin{array}{l}
{\cos x = – 1}\\
{\cos 3x = – 1}
\end{array}} \right.}
\end{array}} \right.
$$
 vi phạm điều kiện vì $\sin x \ne 0.$

Vậy phương trình vô nghiệm.

## Bài 7: Giải phương trình:

$\frac{{\cos x – 2\sin x\cos x}}{{2{{\cos }^2}x – \sin x – 1}} = \sqrt 3 .$

Ta có:

$2{\cos ^2}x – \sin x – 1$ $= – 2{\sin ^2}x – \sin x + 1$ $= (\sin x + 1)(1 – 2\sin x).$

Điều kiện:

$2{\cos ^2}x + \sin x – 1 \ne 0$ $\Leftrightarrow (\sin x + 1)(1 – 2\sin x) \ne 0.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\sin x \ne – 1}\\
{\sin x \ne \frac{1}{2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ne – \frac{\pi }{2} + 2k\pi }\\
{x \ne \frac{\pi }{6} + 2k\pi }\\
{x \ne \frac{{5\pi }}{6} + 2k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Biến đổi phương trình về dạng:

$\frac{{\cos x(1 – 2\sin x)}}{{(\sin x + 1)(1 – 2\sin x)}} = \sqrt 3$ $\Leftrightarrow \cos x = \sqrt 3 \sin x + \sqrt 3 .$

$\Leftrightarrow \sqrt 3 \sin x – \cos x = – \sqrt 3$ $\Leftrightarrow \sin \left( {x – \frac{\pi }{6}} \right) = – \frac{{\sqrt 3 }}{2}.$

$$
\Leftrightarrow \left[ {\begin{array}{c}
{x – \frac{\pi }{6} = – \frac{\pi }{3} + 2k\pi }\\
{x – \frac{\pi }{6} = \frac{{4\pi }}{3} + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – \frac{\pi }{6} + 2k\pi }\\
{x = \frac{{3\pi }}{2} + 2k\pi \:{\rm{(loại)}}}
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có một họ nghiệm.

## Bài 8: Giải phương trình:

$\tan x – \sin 2x – \cos 2x$ $+ 2\left( {2\cos x – \frac{1}{{\cos x}}} \right) = 0.$

Điều kiện:

$\cos x \ne 0 \Leftrightarrow x \ne \frac{\pi }{2} + k\pi$, $k \in Z.$

Biến đổi phương trình về dạng:

$\frac{{\sin x}}{{\cos x}} – 2\sin x\cos x – \cos 2x$ $+ 2\left( {\frac{{2{{\cos }^2}x – 1}}{{\cos x}}} \right) = 0.$

$\Leftrightarrow \sin x\left( {\frac{1}{{\cos x}} – 2\cos x} \right)$ $– \cos 2x + \frac{{2\cos 2x}}{{\cos x}} = 0.$

$\Leftrightarrow – \sin x.\frac{{\cos 2x}}{{\cos x}}$ $– \cos 2x + \frac{{2\cos 2x}}{{\cos x}} = 0$ $\Leftrightarrow \frac{{\cos 2x}}{{\cos x}}( – \sin x – \cos x + 2) = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\cos 2x = 0}\\
{\cos x + \sin x = 2}
\end{array}} \right.
$$
 $\Leftrightarrow x = \frac{\pi }{4} + \frac{{k\pi }}{2}$, $k \in Z.$

Vậy phương trình có một họ nghiệm.

## Bài 9: Giải phương trình:

$1 + \cot 2x = \frac{{1 – \cos 2x}}{{{{\sin }^2}2x}}.$

Điều kiện:

$\sin 2x \ne 0$ $\Leftrightarrow 2x \ne k\pi$ $\Leftrightarrow x \ne \frac{{k\pi }}{2}$, $k \in Z$ $(*).$

Biến đổi phương trình về dạng:

$1 + \frac{{\cos 2x}}{{\sin 2x}} = \frac{{1 – \cos 2x}}{{1 – {{\cos }^2}2x}}$ $\Leftrightarrow \frac{{\cos 2x + \sin 2x}}{{\sin 2x}} = \frac{1}{{1 + \cos 2x}}.$

$\Leftrightarrow (\cos 2x + \sin 2x)(1 + \cos 2x) = \sin 2x.$

$\Leftrightarrow \cos 2x + \sin 2x$ $+ (\cos 2x + \sin 2x)\cos 2x$ $= \sin 2x.$

$\Leftrightarrow (\cos 2x + \sin 2x + 1)\cos 2x = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\cos 2x = 0}\\
{\sqrt 2 \cos \left( {2x – \frac{\pi }{4}} \right) = – 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\cos 2x = 0}\\
{\cos \left( {2x – \frac{\pi }{4}} \right) = – \frac{{\sqrt 2 }}{2}}
\end{array}} \right..
$$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{2x = \frac{\pi }{2} + k\pi }\\
{2x – \frac{\pi }{4} = \pm \frac{{3\pi }}{4} + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \frac{\pi }{4} + \frac{{k\pi }}{2}}\\
{x = \frac{\pi }{2} + k\pi }\\
{x = – \frac{\pi }{4} + k\pi }
\end{array}} \right.
$$
 $\mathop \Leftrightarrow \limits^{(*)} x = \frac{\pi }{4} + \frac{{k\pi }}{2}$, $k \in Z.$

Vậy phương trình có một họ nghiệm.

<!-- chunk:10 level:4 source:https://toanmath.com/2019/08/loai-nghiem-khong-thich-hop-khi-giai-phuong-trinh-luong-giac.html -->
## Bài tập 1. Giải các phương trình sau:

a. $6\sin x – 2{\cos ^3}x = \frac{{5\sin 4x\cos x}}{{2\cos 2x}}.$

b. $\frac{{{{\sin }^4}x + {{\cos }^4}x}}{{\sin 2x}} = \frac{1}{2}(\tan x + \cot x).$

<!-- chunk:11 level:4 source:https://toanmath.com/2019/08/loai-nghiem-khong-thich-hop-khi-giai-phuong-trinh-luong-giac.html -->
## Bài tập 2. Giải các phương trình sau:

a. $\frac{{\sin x + \sin 2x + \sin 3x}}{{\cos x + \cos 2x + \cos 3x}} = \sqrt 3 .$

b. $\frac{{1 + 2{{\sin }^2}x – 3\sqrt 2 \sin x + \sin 2x}}{{2\sin x\cos x – 1}} = 1.$

c. $2(\sin 3x – \cos 3x) = \frac{1}{{\sin x}} + \frac{1}{{\cos x}}.$

d. $\frac{{{{\sin }^3}x + {{\cos }^3}x}}{{2\cos x – \sin x}} = \cos 2x.$

e. $2\sqrt 2 \sin \left( {x + \frac{\pi }{4}} \right) = \frac{1}{{\sin x}} + \frac{1}{{\cos x}}.$

f. $\frac{1}{{\tan x + \cot 2x}} = \frac{{\sqrt 2 (\cos x – \sin x)}}{{\cot x – 1}}.$

g. $\frac{{{{\cot }^2}x – {{\tan }^2}x}}{{\cos 2x}} = 16(1 + \cos 4x).$

<!-- chunk:12 level:4 source:https://toanmath.com/2019/08/loai-nghiem-khong-thich-hop-khi-giai-phuong-trinh-luong-giac.html -->
## Bài tập 3. Giải các phương trình sau:

a. ${\sin ^4}x + {\cos ^4}x$ $= \frac{7}{8}\cot \left( {x + \frac{\pi }{3}} \right)\cot \left( {\frac{\pi }{6} – x} \right).$

b. $\frac{1}{{\cos x}} + \frac{1}{{\sin 2x}} = \frac{2}{{\sin 4x}}.$

<!-- chunk:13 level:4 source:https://toanmath.com/2019/08/loai-nghiem-khong-thich-hop-khi-giai-phuong-trinh-luong-giac.html -->
## Bài tập 4. Giải các phương trình sau:

a. $6\sin x – 2{\cos ^3}x = \frac{{5\sin 4x\cos x}}{{2\cos 2x}}.$

b. ${\sin ^2}x – \sin x + \frac{1}{{{{\sin }^2}x}} – \frac{1}{{\sin x}} = 0.$

<!-- chunk:14 level:4 source:https://toanmath.com/2019/08/loai-nghiem-khong-thich-hop-khi-giai-phuong-trinh-luong-giac.html -->
## Bài tập 8. Tìm tổng các nghiệm thoả mãn $1 \le x \le \pi$ của phương trình:

$\cos 2x – {\tan ^2}x = \frac{{{{\cos }^2}x – {{\cos }^3}x – 1}}{{{{\cos }^2}x}}.$