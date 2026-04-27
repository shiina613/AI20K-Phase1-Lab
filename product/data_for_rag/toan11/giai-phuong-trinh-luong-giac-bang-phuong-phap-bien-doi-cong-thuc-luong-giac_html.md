# Giải phương trình lượng giác bằng phương pháp biến đổi công thức lượng giác

<!-- chunk:0 level:0 source:https://toanmath.com/2018/06/giai-phuong-trinh-luong-giac-bang-phuong-phap-bien-doi-cong-thuc-luong-giac.html -->
Bài viết hướng dẫn cách giải phương trình lượng giác bằng phương pháp biến đổi công thức lượng giác thông qua các ví dụ minh họa có lời giải chi tiết.

**1. Sử dụng các phép biến đổi góc lượng giác**

Khi giải phương trình lượng giác cần xem xét mối quan hệ giữa các góc (cung) để từ đó kết hợp với các phép biến đổi góc đặc biệt, công thức cộng lượng giác … để đưa về dạng góc cơ bản.

<!-- chunk:1 level:3 source:https://toanmath.com/2018/06/giai-phuong-trinh-luong-giac-bang-phuong-phap-bien-doi-cong-thuc-luong-giac.html -->
## Ví dụ 1. Giải các phương trình lượng giác sau:

a. $\frac{1}{{\sin x}} + \frac{1}{{\sin \left( {x – \frac{{3\pi }}{2}} \right)}}$ $= 4\sin \left( {\frac{{7\pi }}{4} – x} \right).$

b. ${\sin ^4}x + {\cos ^4}x$ $= \frac{7}{8}\cot \left( {x + \frac{\pi }{3}} \right)\cot \left( {\frac{\pi }{6} – x} \right).$

c. $\frac{{{{\sin }^4}2x + {{\cos }^4}2x}}{{\tan \left( {\frac{\pi }{4} – x} \right)\tan \left( {\frac{\pi }{4} + x} \right)}}$ $= {\cos ^4}4x.$

a. Nhận xét: Từ sự xuất hiện hai cung $x – \frac{{3\pi }}{2}$ và $\frac{{7\pi }}{4} – x$ mà chúng ta liên tưởng đến việc đưa đưa $2$ cung này về cùng một cung $x$. Để làm được điều đó ta có thể sử dụng công thức cộng cung hoặc công thức về các góc đặc biệt.

Điều kiện: $\sin x \ne 0$, $\cos x \ne 0$ $\Leftrightarrow \sin 2x \ne 0$ $\Leftrightarrow x \ne k\frac{\pi }{2},k \in Z.$

$PT \Leftrightarrow \frac{1}{{\sin x}} + \frac{1}{{\cos x}}$ $= – 2\sqrt 2 \left( {\cos x + \sin x} \right)$ $\Leftrightarrow \left( {\sin x + \cos x} \right)\left( {\sqrt 2 \sin 2x + 1} \right) = 0.$

Kết hợp với điều kiện ta được nghiệm phương trình là: $x = – \frac{\pi }{4} + k\pi$, $x = – \frac{\pi }{8} + k\pi$, $x = \frac{{5\pi }}{8} + k\pi$ $\left( {k \in Z} \right).$

b. Điều kiện: $\sin \left( {x + \frac{\pi }{3}} \right).\sin \left( {\frac{\pi }{6} – x} \right) \ne 0$ $\Leftrightarrow \cos \left( {2x + \frac{\pi }{6}} \right) \ne \cos \frac{\pi }{2} = 0.$

Do $\left( {x + \frac{\pi }{3}} \right) + \left( {\frac{\pi }{6} – x} \right) = \frac{\pi }{2}$ nên $PT \Leftrightarrow {\sin ^4}x + {\cos ^4}x = \frac{7}{8}$ $\Leftrightarrow 1 – \frac{1}{2}{\sin ^2}2x = \frac{7}{8}$ $\Leftrightarrow \sin 2x = \pm \frac{1}{2}$. Kết hợp với điều kiện ta được: $x = \pm \frac{\pi }{{12}} + k\frac{\pi }{2}$ $\left( {k \in Z} \right).$

c. Nhận xét: Từ tổng hai cung $\left( {\frac{\pi }{4} – x} \right) + \left( {\frac{\pi }{4} + x} \right) = \frac{\pi }{2}$ nên $\tan \left( {\frac{\pi }{4} – x} \right)\tan \left( {\frac{\pi }{4} + x} \right) = 1.$

Điều kiện 1: $\cos \left( {\frac{\pi }{4} – x} \right)\cos \left( {\frac{\pi }{4} + x} \right) \ne 0$ $\Leftrightarrow \frac{1}{2}\left( {\cos 2x + \cos \frac{\pi }{2}} \right) \ne 0$ $\Leftrightarrow \cos 2x \ne 0.$

Điều kiện 2: $\sin \left( {\frac{\pi }{4} – x} \right)\sin \left( {\frac{\pi }{4} + x} \right) \ne 0$ $\Leftrightarrow \frac{1}{2}\left( {\cos 2x – \cos \frac{\pi }{2}} \right) \ne 0$ $\Leftrightarrow \cos 2x \ne 0.$

$PT \Leftrightarrow {\sin ^4}2x + {\cos ^4}2x = {\cos ^4}4x$ $\Leftrightarrow 1 – \frac{1}{2}{\sin ^2}4x = {\cos ^4}4x$ $\Leftrightarrow 2{\cos ^4}4x – {\cos ^2}4x – 1 = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
{\cos ^2}4x = 1\\
{\cos ^2}4x = – \frac{1}{2}\left( {loại} \right)
\end{array} \right.
$$
 $\Leftrightarrow \sin 4x = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
\sin 2x = 0\\
\cos 2x = 0\left( {loại} \right)
\end{array} \right.
$$

Vậy phương trình có nghiệm $x = k\frac{\pi }{2}.$

2. Sử dụng công thức biến đổi tổng thành tích và công thức biến đổi tích thành tổng
Khi giải phương trình lượng giác mà gặp dạng tổng (hoặc hiệu) của $sin$ (hoặc $cos$) với nhiều cung khác nhau ta cần để ý đến các cung có tổng (hiệu) các góc bằng nhau để áp dụng công thức tổng sang tích.

<!-- chunk:2 level:3 source:https://toanmath.com/2018/06/giai-phuong-trinh-luong-giac-bang-phuong-phap-bien-doi-cong-thuc-luong-giac.html -->
## Ví dụ 2. Giải các phương trình lượng giác sau:

a. $\sin x + \sin 2x + \sin 3x$ $+ \sin 4x + \sin 5x + \sin 6x = 0.$

b. $\cos 3x{\cos ^3}x – \sin 3x{\sin ^3}x$ $= \frac{{2 – 3\sqrt 2 }}{8}.$

c. $1 + \sin x + \cos 3x$ $= \cos x + \sin 2x + \cos 2x.$

d. ${\cos ^3}x + {\sin ^3}x$ $= \sin 2x + \sin x + \cos x.$

a. Nhận xét: Bài toán có các cung khác nhau biểu diễn dưới dạng tổng (hiệu) của các hàm số $sin$ (hàm số $cos$) ta nên ghép các số hạng này thành cặp sao cho tổng (hiệu) các cung của chúng bằng nhau, cụ thể trong trường hợp này ta để ý: $x + 6x$ $= 2x + 5x$ $= 3x + 4x.$ Tại sao lại cần phải ghép như vậy? Lý do là chúng ta cần xuất hiện thừa số chung để nhóm ra ngoài, đưa bài toán về dạng tích.

$PT \Leftrightarrow \left( {\sin 6x + \sin x} \right)$ $+ \left( {\sin 5x + \sin 2x} \right) + \left( {\sin 4x + \sin 3x} \right) = 0$

$\Leftrightarrow 2\sin \frac{{7x}}{2}\left( {\cos \frac{{5x}}{2} + \cos \frac{x}{2} + \cos \frac{{3x}}{2}} \right) = 0$ $\Leftrightarrow 4\sin \frac{{7x}}{2}\cos \frac{{3x}}{2}\left( {2\cos x + 1} \right) = 0.$

Vậy phương trình có nghiệm $x = \frac{{k2\pi }}{7}$, $x = \frac{\pi }{3} + \frac{{k2\pi }}{3}$, $x = \pm \frac{{2\pi }}{3} + k2\pi$ $\left( {k \in Z} \right).$

b. Ta có thể giải phương trình này bằng cách sử dụng công thức nhân ba của $sin$ và $cos$ nhưng lời giải sẽ phức tạp hơn. Chính vì thế mà ta khéo léo phân tích để áp dụng công thức tích sang tổng.

$PT \Leftrightarrow \frac{1}{2}\left( {\cos 4x + \cos 2x} \right){\cos ^2}x$ $+ \frac{1}{2}\left( {\cos 4x – \cos 2x} \right){\sin ^2}x$ $= \frac{{2 – 3\sqrt 2 }}{8}$

$\Leftrightarrow \cos 4x\left( {{{\sin }^2}x + {{\cos }^2}x} \right)$ $+ \cos 2x\left( {{{\cos }^2}x – {{\sin }^2}x} \right)$ $= \frac{{2 – 3\sqrt 2 }}{4}$ $\Leftrightarrow \cos 4x + {\cos ^2}2x = \frac{{2 – 3\sqrt 2 }}{4}$

$\Leftrightarrow \cos 4x = – \frac{{\sqrt 2 }}{2}$ $\Leftrightarrow x = \pm \frac{{3\pi }}{{16}} + k\frac{\pi }{2}$ $(k ∈ Z).$

c. $PT \Leftrightarrow 1 – \cos 2x + \sin x$ $– \sin 2x + \cos 3x – \cos x = 0$

$\Leftrightarrow 2{\sin ^2}x + \sin x$ $– 2\sin x\cos x – 2\sin 2x\sin x = 0$

$\Leftrightarrow \sin x\left( {2\sin x – 2\cos x – 2\sin 2x + 1} \right) = 0$

$$
\Leftrightarrow \left[ \begin{array}{l}
\sin x = 0\\
2\left( {\sin x – \cos x} \right) – 4\sin x\cos x + 1 = 0
\end{array} \right.
$$

Đáp số: $x = k\pi$, $x = \pm \frac{\pi }{3} + k2\pi$, $x = – \frac{\pi }{6} + k2\pi$, $x = \frac{{7\pi }}{6} + k2\pi$ $(k ∈ Z).$

d. $PT \Leftrightarrow 2\sin x\cos x + \sin x$ $– {\sin ^3}x + \cos x – {\cos ^3}x = 0$

$\Leftrightarrow 2\sin x\cos x + \sin x{\cos ^2}x$ $+ \cos x{\sin ^2}x = 0$ $\Leftrightarrow \sin x\cos x\left( {2 + \sin x + \cos x} \right) = 0.$

Đáp số: $x = k\frac{\pi }{2}$ $(k ∈ Z).$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/06/giai-phuong-trinh-luong-giac-bang-phuong-phap-bien-doi-cong-thuc-luong-giac.html -->
## Ví dụ 3. Giải các phương trình lượng giác sau:

a. $\sin 2x\sin 5x = \sin 3x\sin 4x.$

b. ${\cos ^4}x + {\sin ^4}x$ $+ \cos \left( {x – \frac{\pi }{4}} \right)\sin \left( {3x – \frac{\pi }{4}} \right)$ $– \frac{3}{2} = 0.$

c. $\sqrt 3 \cos 5x – 2\sin 3x\cos 2x – \sin x = 0.$

d. $\sin x + \cos x\sin 2x + \sqrt 3 \cos 3x$ $= 2\left( {\cos 4x + {{\sin }^3}x} \right).$

a. $PT \Leftrightarrow \frac{1}{2}\left( {\cos 7x – \cos 3x} \right)$ $= \frac{1}{2}\left( {\cos 7x – \cos x} \right)$ $\Leftrightarrow \cos 3x = \cos x$ $\Leftrightarrow 3x = \pm x + k2\pi$ $\Leftrightarrow x = k\frac{\pi }{2}$ $(k ∈ Z).$

b. $PT \Leftrightarrow 1 – \frac{1}{2}{\sin ^2}2x$ $+ \frac{1}{2}\left( {\sin \left( {4x – \frac{\pi }{2}} \right) + \sin 2x} \right)$ $– \frac{3}{2} = 0$

$\Leftrightarrow {\sin ^2}2x + \sin 2x – 2 = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
\sin 2x = 1\\
\sin 2x = – 2\left( {loại} \right)
\end{array} \right.
$$
 $\Leftrightarrow x = \frac{\pi }{4} + k\pi$ $\left( {k \in Z} \right).$

c. Nhận xét: Từ sự xuất hiện các cung $5x,3x,2x,x$ và $3x + 2x = 5x$ ta nghĩ ngay đến việc áp dụng công thức tích sang tổng để đưa về cung $5x$. Còn cung $x$ thì xử lý thế nào, ta quan sát lời giải sau:

$PT \Leftrightarrow \sqrt 3 \cos 5x – \sin 5x$ $– \sin x – \sin x = 0$ $\Leftrightarrow \frac{{\sqrt 3 }}{2}\cos 5x – \frac{1}{2}\sin 5x = \sin x$

$\Leftrightarrow \sin \left( {\frac{\pi }{3} – 5x} \right) = \sin x$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = \frac{\pi }{{12}} – k\frac{\pi }{3}\\
x = – \frac{\pi }{6} – k\frac{\pi }{2}
\end{array} \right.
$$
 $(k ∈ Z).$

Vậy phương trình có nghiệm: $x = \frac{\pi }{{12}} – k\frac{\pi }{3}$, $x = – \frac{\pi }{6} – k\frac{\pi }{2}$ $\left( {k \in Z} \right).$

Chú ý: Đối với dạng phương trình $a\sin x + b\cos x$ $= a’\sin kx + b’\cos kx$, $k \ne 0,1$ ta coi như $2$ vế của phương trình là $2$ phương trình bậc nhất với $sin$ và $cos$, do đó ta có cách làm tương tự.

d. $PT \Leftrightarrow \sin x\left( {1 – 2{{\sin }^2}x} \right)$ $+ \cos x\sin 2x + \sqrt 3 \cos 3x$ $= 2\cos 4x$

$\Leftrightarrow \sin 3x + \sqrt 3 \cos 3x = 2\cos 4x$ $\Leftrightarrow \frac{1}{2}\sin 3x + \frac{{\sqrt 3 }}{2}\cos 3x = \cos 4x$

$\Leftrightarrow \cos 4x = \cos \left( {3x – \frac{\pi }{6}} \right)$ $\Leftrightarrow 4x = \pm \left( {3x – \frac{\pi }{6}} \right) + k2\pi$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = – \frac{\pi }{6} + k2\pi \\
x = \frac{\pi }{{42}} + k\frac{{2\pi }}{7}
\end{array} \right.\left( {k \in Z} \right).
$$

[ads]

3. Sử dụng công thức hạ bậc
Khi giải các phương trình lượng giác mà bậc của $sin$ và $cos$ là bậc chẵn ta thường hạ bậc từ đó đưa về phương trình cơ bản.

<!-- chunk:4 level:3 source:https://toanmath.com/2018/06/giai-phuong-trinh-luong-giac-bang-phuong-phap-bien-doi-cong-thuc-luong-giac.html -->
## Ví dụ 4. Giải các phương trình lượng giác sau:

a. ${\sin ^2}x + {\sin ^2}2x + {\sin ^2}3x = \frac{3}{2}.$

b. ${\sin ^2}3x – {\cos ^2}4x = {\sin ^2}5x – {\cos ^2}6x.$

c. ${\sin ^2}\left( {\frac{x}{2} – \frac{\pi }{4}} \right){\tan ^2}x – {\cos ^2}\frac{x}{2} = 0.$

d. ${\cos ^2}3x\cos 2x – {\cos ^2}x = 0.$

a. Từ sự xuất hiện bậc chẵn của hàm số $sin$ và tổng hai cung $\frac{{6x + 2x}}{2} = 4x$ mà ta nghĩ đến việc hạ bậc và sử dụng công thức biến tổng sang tích sau đó nhóm các hạng tử để đưa về phương trình tích.

$PT \Leftrightarrow \cos 2x + \cos 4x + \cos 6x = 0$ $\Leftrightarrow \cos 4x\left( {2\cos 2x + 1} \right) = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
\cos 4x = 0\\
\cos 2x = – \frac{1}{2}
\end{array} \right.
$$

Vậy phương trình có nghiệm: $x = \frac{\pi }{8} + \frac{{k\pi }}{4}$, $x = \pm \frac{\pi }{3} + k\pi$ $(k ∈ Z).$

b. $PT \Leftrightarrow \frac{{1 – \cos 6x}}{x} – \frac{{1 + \cos 8x}}{2}$ $= \frac{{1 – \cos 10x}}{2} – \frac{{1 + \cos 12x}}{2}$

$\Leftrightarrow \left( {\cos 12x + \cos 10x} \right)$ $- \left( {\cos 8x + \cos 6x} \right) = 0$ $\Leftrightarrow 2\cos 11x\cos x – 2\cos 7x\cos x = 0$

$\Leftrightarrow \cos x\left( {\cos 11x – \cos 7x} \right) = 0$ $\Leftrightarrow \cos x\sin 9x\sin 2x = 0.$

Vậy phương trình có nghiệm: $x = k\frac{\pi }{9}$, $x = k\frac{\pi }{2}$ $\left( {k \in Z} \right).$

c. Điều kiện: $\cos x \ne 0.$

$PT \Leftrightarrow \frac{1}{2}\left[ {1 – \cos \left( {x – \frac{\pi }{2}} \right)} \right]\frac{{{{\sin }^2}x}}{{{{\cos }^2}x}}$ $= \frac{1}{2}\left( {1 + \cos x} \right)$ $\Leftrightarrow \left( {1 – \sin x} \right){\sin ^2}x = \left( {1 + \cos x} \right){\cos ^2}x$

$\Leftrightarrow \left( {1 – \sin x} \right)\left( {1 + \cos x} \right)\left( {\sin x + \cos x} \right) = 0.$

Đáp số: Kết hợp với điều kiện ta được: $x = \pi + k2\pi$, $x = – \frac{\pi }{4} + k\pi$ $\left( {k \in Z} \right).$

d. $PT \Leftrightarrow \frac{{1 + \cos 6x}}{2}\cos 2x$ $– \frac{{1 + \cos 2x}}{2} = 0$ $\Leftrightarrow \cos 6x.\cos 2x – 1 = 0$

$\Leftrightarrow \cos 8x + \cos 4x – 2 = 0$ $\Leftrightarrow 2{\cos ^2}4x + \cos 4x – 3 = 0$ $\Leftrightarrow \cos 4x = 1 \Leftrightarrow x = k\frac{\pi }{2}$ $\left( {k \in Z} \right).$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/06/giai-phuong-trinh-luong-giac-bang-phuong-phap-bien-doi-cong-thuc-luong-giac.html -->
## Ví dụ 5. Giải các phương trình lượng giác sau:

a. $2{\sin ^2}2x + \sin 7x – 1 = \sin x.$

b. ${\cos ^4}x + {\sin ^4}\left( {x + \frac{\pi }{4}} \right) = 1.$

c. $\left( {2 – \sqrt 3 } \right)\cos x – 2{\sin ^2}\left( {\frac{x}{2} – \frac{\pi }{4}} \right)$ $= 2\cos x – 1.$

d. $3{\tan ^3}x – \tan x + \frac{{3\left( {1 + \sin x} \right)}}{{{{\cos }^2}x}}$ $– 8{\cos ^2}\left( {\frac{\pi }{4} – \frac{x}{2}} \right) = 0.$

a. $PT \Leftrightarrow \sin 7x – \sin x$ $– \left( {1 – 2{{\sin }^2}2x} \right) = 0$ $\Leftrightarrow 2\cos 4x.\sin 3x – \cos 4x = 0$ $\Leftrightarrow \cos 4x\left( {2\sin 3x – 1} \right) = 0.$

Vậy phương trình có nghiệm: $x = \frac{\pi }{8} + k\frac{\pi }{4}$, $x = \frac{\pi }{{18}} + k\frac{{2\pi }}{3}$, $x = \frac{{5\pi }}{{18}} + k\frac{{2\pi }}{3}$ $(k∈Z).$

b. ${\left( {1 + \cos 2x} \right)^2} + {\left( {1 + \sin 2x} \right)^2} = 1$ $\Leftrightarrow \sin 2x + \cos 2x = – 1$

$\Leftrightarrow \sqrt 2 \cos \left( {2x – \frac{\pi }{2}} \right) = – 1$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = \frac{\pi }{2} + k\pi \\
x = – \frac{\pi }{4} + k\pi
\end{array} \right.\left( {k \in Z} \right)
$$

c. $PT \Leftrightarrow – \sqrt 3 \cos x + \sin x = 0$ $\Leftrightarrow \frac{1}{2}\sin x – \frac{{\sqrt 3 }}{2}\cos x = 0$ $\Leftrightarrow \sin \left( {x – \frac{\pi }{3}} \right) = 0$ $\Leftrightarrow x = \frac{\pi }{3} + k\pi$ $(k∈Z).$

d. $PT \Leftrightarrow 3{\tan ^3}x – \tan x$ $+ \frac{{3\left( {1 + \sin x} \right)}}{{{{\cos }^2}x}} – 4\left( {1 + \sin x} \right) = 0$

$\Leftrightarrow \tan x\left( {3{{\tan }^2}x – 1} \right)$ $+ \left( {1 + \sin x} \right)\left( {3{{\tan }^2}x – 1} \right) = 0$ $\Leftrightarrow \left( {3{{\tan }^2}x – 1} \right)\left( {\tan x + 1 + \sin x} \right) = 0$

Trường hợp 1: $\tan x = \pm \frac{1}{{\sqrt 3 }}$ $\Leftrightarrow x = \pm \frac{\pi }{6} + k\pi$ $\left( {k \in Z} \right).$

Trường hợp 2: $1 + \sin x + \tan x = 0$ $\Leftrightarrow \sin x + \cos x + \sin x\cos x = 0$ (phương trình đối xứng với $sin$ và $cos$).

Giải phương trình này được: $x = \frac{\pi }{4} \pm \arccos \left( {\frac{{\sqrt 2 – 1}}{2}} \right) + k2\pi$ $\left( {k \in Z} \right).$

4. Sử dụng các đẳng thức lượng giác quan trọng (hằng đẳng thức)
Ví dụ 6. Giải các phương trình lượng giác sau:

a. ${\left( {\sin \frac{x}{2} + \cos \frac{x}{2}} \right)^2} + \sqrt 3 \cos x = 2.$

b. $\cot x – \tan x + 4\sin 2x = \frac{2}{{\sin 2x}}.$

c. $\tan x = \cot x + 2{\cot ^3}2x.$

d. $\tan x + \cot x = 2\left( {\sin 2x + \cos 2x} \right).$

a. $PT \Leftrightarrow 1 + 2\sin \frac{x}{2}\cos \frac{x}{2}$ $+ \sqrt 3 \cos x = 2$ $\Leftrightarrow \sin x + \sqrt 3 \cos x = 2$

$\Leftrightarrow \frac{1}{2}\sin x + \frac{{\sqrt 3 }}{2}\cos x = 1$ $\Leftrightarrow \sin \left( {x + \frac{\pi }{3}} \right) = \frac{1}{2}$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = – \frac{\pi }{6} + k2\pi \\
x = \frac{\pi }{2} + k2\pi
\end{array} \right.
$$
 $\left( {k \in Z} \right).$

b. Nhận xét: Từ sự xuất hiện của $\cot x – \tan x$ và $\sin 2x$ ta xem chúng có mối quan hệ nào?

Ta có: $\cot x – \tan x$ $= \frac{{{{\cos }^2}x – {{\sin }^2}x}}{{\sin x\cos x}}$ $= 2\frac{{\cos 2x}}{{\sin 2x}}$. Từ đó ta định hướng giải cho bài toán như sau:

Điều kiện: $\sin 2x \ne 0 \Leftrightarrow x \ne k\frac{\pi }{2}.$

$PT \Leftrightarrow 2\frac{{\cos 2x}}{{\sin 2x}} + 4\sin 2x$ $= \frac{2}{{\sin 2x}}\cos 2x + 2{\sin ^2}2x = 1$ $\Leftrightarrow 2{\cos ^2}2x – \cos 2x – 1 = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
\cos 2x = 1\\
\cos 2x = – \frac{1}{2}
\end{array} \right.
$$
 $\Leftrightarrow x = \pm \frac{\pi }{3} + k\pi$ $(k∈Z).$

Chú ý: Ta có thể đặt $t = \tan x$ $\Rightarrow \cot x = \frac{1}{t}$, $\sin 2x = \frac{{2t}}{{1 – {t^2}}}$ đưa phương trình về ẩn $t$ để giải.

c. Điều kiện: $\sin 2x \ne 0 \Leftrightarrow x \ne k\frac{\pi }{2}.$

$PT \Leftrightarrow \frac{{\sin x}}{{\cos x}} – \frac{{\cos x}}{{\sin x}} = 2{\cot ^3}2x$ $\Leftrightarrow – 2\frac{{\cos 2x}}{{\sin 2x}} = 2{\cot ^3}2x$ $\Leftrightarrow \cot 2x + {\cot ^3}2x = 0$

$\Leftrightarrow \cot 2x = 0$ $\Leftrightarrow x = \frac{\pi }{4} + k\frac{\pi }{2}$ $(k∈Z).$

d. Điều kiện: $\sin 2x \ne 0 \Leftrightarrow x \ne k\frac{\pi }{2}.$

$PT \Leftrightarrow \frac{{\sin x}}{{\cos x}} + \frac{{\cos x}}{{\sin x}}$ $= 2\left( {\sin 2x + \cos 2x} \right)$ $\Leftrightarrow \frac{2}{{\sin 2x}} = 2\left( {\sin 2x + \cos 2x} \right)$

$\Leftrightarrow 1 = {\sin ^2}2x + \sin 2x\cos 2x$ $\Leftrightarrow {\cos ^2}2x = \sin 2x\cos 2x$

$$
\Leftrightarrow \left[ \begin{array}{l}
\cos 2x = 0\\
\tan 2x = 1
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = \frac{\pi }{4} + k\frac{\pi }{2}\\
x = \frac{\pi }{8} + k\frac{\pi }{2}
\end{array} \right.
$$
 $\left( {k \in Z} \right).$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/06/giai-phuong-trinh-luong-giac-bang-phuong-phap-bien-doi-cong-thuc-luong-giac.html -->
## Ví dụ 7. Giải các phương trình lượng giác sau:

a. ${\cos ^6}x – {\sin ^6}x = \frac{{13}}{8}{\cos ^2}2x.$

b. $\frac{{2\left( {{{\cos }^6}x + {{\sin }^6}x} \right) – \sin x\cos x}}{{\sqrt 2 – 2\sin x}} = 0.$

c. $\frac{{{{\cos }^4}x + {{\sin }^4}x}}{{5\sin 2x}}$ $= \frac{1}{2}\cot 2x – \frac{1}{{8\sin 2x}}.$

d. $\cot x = \tan x + \frac{{2\cos 4x}}{{\sin 2x}}.$

a. Nhận xét: Xuất hiện ${\cos ^6}x – {\sin ^6}x$ ta nghĩ đến việc sử dụng hằng đẳng thức ${a^3} – {b^3}.$

$PT \Leftrightarrow \left( {{{\cos }^2}x – {{\sin }^2}x} \right)\left( {{{\cos }^4}x + {{\sin }^4}x + {{\sin }^2}x{{\cos }^2}x} \right)$ $= \frac{{13}}{8}{\cos ^2}2x$

$\Leftrightarrow \cos 2x\left( {1 – \frac{1}{2}{{\sin }^2}2x + \frac{1}{4}{{\sin }^2}2x} \right)$ $= \frac{{13}}{8}{\cos ^2}2x$ $\Leftrightarrow \cos 2x\left( {8 – 2{{\sin }^2}2x – 13\cos 2x} \right) = 0$
\Leftrightarrow \left[ \begin{array}{l}
\cos 2x = 0\\
2{\cos ^2}2x – 13\cos 2x + 6 = 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
\cos 2x = 0\\
\cos 2x = \frac{1}{2}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = \frac{\pi }{4} + k\frac{\pi }{2}\\
x = \pm \frac{\pi }{6} + k\pi
\end{array} \right.
$\left( {k \in Z} \right).$

b. Điều kiện: $\sin x \ne \frac{1}{{\sqrt 2 }}$
\Leftrightarrow \left\{ \begin{array}{l}
x \ne \frac{\pi }{4} + k2\pi \\
x \ne \frac{{3\pi }}{4} + k2\pi
\end{array} \right.
$$

$PT \Leftrightarrow 2\left( {{{\cos }^4}x + {{\sin }^4}x – {{\sin }^2}x{{\cos }^2}x} \right)$ $– \sin x\cos x = 0$

$\Leftrightarrow 2 – 6{\sin ^2}x{\cos ^2}x – \sin x\cos x = 0$

$\Leftrightarrow 3{\sin ^2}2x + \sin 2x – 4 = 0$ $\Leftrightarrow \sin 2x = 1$ $\Leftrightarrow x = \frac{\pi }{4} + k\pi$ $(k∈Z).$

Kết hợp với điều kiện ta được nghiệm của phương trình là: $x = \frac{{5\pi }}{4} + k2\pi$ $\left( {k \in Z} \right).$

c. Điều kiện: $\sin 2x \ne 0 \Leftrightarrow x \ne k\frac{\pi }{2}.$

$PT \Leftrightarrow \frac{{1 – \frac{1}{2}{{\sin }^2}2x}}{{5\sin 2x}}$ $= \frac{1}{2}\frac{{\cos 2x}}{{\sin 2x}} – \frac{1}{{8\sin 2x}}$ $\Leftrightarrow {\cos ^2}2x – 5\cos 2x + \frac{9}{4} = 0$

$\Leftrightarrow \cos 2x = \frac{1}{2}$ $\Leftrightarrow x = \pm \frac{\pi }{6} + k\pi$ $(k∈Z).$

d. Điều kiện: $\sin 2x \ne 0 \Leftrightarrow x \ne k\frac{\pi }{2}.$

$PT \Leftrightarrow \frac{{2\cos 2x}}{{\sin 2x}} = \frac{{2\cos 4x}}{{\sin 2x}}$ $\Leftrightarrow 2{\cos ^2}2x – \cos 2x – 1 = 0$ $\Leftrightarrow \cos 2x = – \frac{1}{2}$ $\Leftrightarrow x = \pm \frac{{2\pi }}{3} + k\pi$ $(k∈Z).$