# Tính tích phân bằng phương pháp đổi biến số

<!-- chunk:0 level:0 source:https://toanmath.com/2018/06/tinh-tich-phan-bang-phuong-phap-doi-bien-so.html -->
Bài viết hướng dẫn tính tích phân bằng phương pháp đổi biến số, gồm đổi biến số dạng 1, đổi biến số dạng 2 và một số bài toán sử dụng phương pháp đổi biến số đặc biệt; trong mỗi phương pháp đều trình bày cụ thể các bước giải và ví dụ minh họa có lời giải chi tiết.

Cơ sở của phương pháp tính tích phân bằng cách đổi biến số là công thức:

$\int\limits_a^b {f[u(x)]u'(x)dx} = \int\limits_\alpha ^\beta {f(u)du}$ với $α = u(a)$ và $β = u(b).$

Từ đó, chúng ta có hai phương pháp đổi biến số sau:

Tính tích phân bằng phương pháp đổi biến số dạng 1

Để tính tích phân: $I = \int\limits_a^b {g(x)dx}$ ta thực hiện các bước:

Bước 1: Chọn biến số:

+ Phân tích $g(x)dx = f[u(x)]u'(x)dx$ $= f[u(x)]d[u(x)].$

+ Đặt $u = u(x).$

Bước 2: Thực hiện phép đổi cận:

+ Với $x = a$ thì $u = u(a).$

+ Với $x = b$ thì $u = u(b).$

Bước 3: Khi đó: $\int\limits_a^b {g(x)dx}$ $= \int\limits_{u(a)}^{u(b)} {f(u)du} .$

<!-- chunk:1 level:3 source:https://toanmath.com/2018/06/tinh-tich-phan-bang-phuong-phap-doi-bien-so.html -->
## Ví dụ 1: Tính các tích phân sau:

a. $\int\limits_0^1 {{x^3}{{(1 + {x^4})}^3}dx} .$

b. $\int\limits_0^1 {\frac{{5xdx}}{{{{({x^2} + 4)}^2}}}} .$

a. Đặt $u = 1 + x^4$, suy ra $du = 4x^3dx.$

Đổi cận: Với $x = 0$ thì $u = 1$, với $x = 1$ thì $u = 2.$

Từ đó: $\int\limits_0^1 {{x^3}{{(1 + {x^4})}^3}dx}$ $= \frac{1}{4}\int\limits_1^2 {{u^3}du}$ $= \frac{1}{{16}}\left. {{u^4}} \right|_1^2$ $= \frac{{15}}{{16}}.$

b. Đặt $u = x^2 + 4$, suy ra $du = 2xdx.$

Đổi cận: Với $x = 0$ thì $u = 4$, với $x = 1$ thì $u = 5.$

Từ đó: $\int\limits_0^1 {\frac{{5x}}{{{{({x^2} + 4)}^2}}}dx}$ $= \frac{5}{2}\int\limits_4^5 {\frac{{du}}{{{u^2}}}}$ $= \left. { – \frac{5}{{2u}}} \right|_4^5$ $= \frac{1}{8}.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/06/tinh-tich-phan-bang-phuong-phap-doi-bien-so.html -->
## Ví dụ 2: Tính các tích phân sau:

a. $\int\limits_0^{\pi /6} {(1 – \cos 3x)\sin 3xdx} .$

b. $\int\limits_0^{\pi /4} {\frac{{\tan x.dx}}{{{{\cos }^2}x}}} .$

a. Đặt $u = 1 – cos3x$, suy ra $du = 3sin3x.dx.$

Đổi cận: Với $x = 0$ thì $u = 0$, với $x = \frac{\pi }{6}$ thì $u = 1.$

Từ đó: $\int\limits_0^{\frac{\pi }{6}} {(1 – \cos 3x)\sin 3xdx}$ $= \frac{1}{3}\int\limits_0^1 {udu}$ $= \frac{1}{6}{u^2}\left| {_0^1} \right.$ $= \frac{1}{6}.$

b. Đặt $u = tanx$, suy ra $du = \frac{{dx}}{{{{\cos }^2}x}}.$

Đổi cận: Với $x = 0$ thì $u = 0$, với $x = \frac{\pi }{4}$ thì $u = 1.$

Từ đó: $\int\limits_0^{\frac{\pi }{4}} {\frac{{\tan x}}{{{{\cos }^2}x}}dx}$ $= \int\limits_0^1 {udu}$ $= \frac{1}{2}{u^2}\left| {_0^1} \right.$ $= \frac{1}{2}.$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/06/tinh-tich-phan-bang-phuong-phap-doi-bien-so.html -->
## Ví dụ 3: Tính các tích phân sau:

a. $\int\limits_0^{\sqrt 3 } {x\sqrt {1 + {x^2}} dx} .$

b. $\int\limits_0^{\sqrt 3 } {{x^5}\sqrt {1 + {x^2}} } dx.$

a. Ta có thể trình bày theo các cách sau:

Cách 1: Đặt $u = \sqrt {{x^2} + 1}$, suy ra: $u^2 = x^2 + 1$ $⇒ 2udu = 2xdx$ $⇒ udu = xdx.$

Đổi cận: Với $x = 0$ thì $u = 1$, với $x = \sqrt 3$ thì $u = 2.$

Từ đó: $\int\limits_0^{\sqrt 3 } {x\sqrt {1 + {x^2}} dx}$ $= \int\limits_1^2 {{u^2}du}$ $= \frac{1}{3}\left. {{u^3}} \right|_1^2$ $= \frac{7}{3}.$

Cách 2: Đặt $u = x^2 + 1$, suy ra $du = 2xdx.$

Đổi cận: Với $x = 0$ thì $u = 1$, với $x = \sqrt 3$ thì $u = 4.$

Từ đó: $\int\limits_0^{\sqrt 3 } {x\sqrt {1 + {x^2}} dx}$ $= \frac{1}{2}\int\limits_1^4 {\sqrt u du}$ $= \frac{1}{3}\left. {{u^{3/2}}} \right|_1^4$ $= \frac{7}{3}.$

Cách 3: Thực hiện phép biến đổi:

$\int\limits_0^{\sqrt 3 } {x\sqrt {1 + {x^2}} dx}$ $= \frac{1}{2}\int\limits_0^{\sqrt 3 } {\sqrt {1 + {x^2}} d(1 + {x^2})}$ $= \frac{1}{2}\int\limits_0^{\sqrt 3 } {{{(1 + {x^2})}^{\frac{1}{2}}}d(1 + {x^2})}$ $= \frac{1}{3}\left. {{{(1 + {x^2})}^{3/2}}} \right|_0^{\sqrt 3 }$ $= \frac{7}{3}.$

b. Đặt $u = \sqrt {1 + {x^2}}$ $⇔ u^2 = 1 + x^2$ $⇔ 2udu = 2xdx.$

Đổi cận: Với $x = 0$ thì $u = 1$, với $x = \sqrt 3$ thì $u = 2.$

Khi đó: $\int\limits_0^{\sqrt 3 } {{x^5}\sqrt {1 + {x^2}} } dx$ $= \int\limits_1^2 {{{({u^2} – 1)}^2}{u^2}} du$ $= \int\limits_1^2 {({u^6} – 2{u^4} + {u^2})} du$ 
$$
= \left( {\frac{1}{7}{u^7} – \frac{2}{5}{u^5} + \frac{1}{3}{u^3}} \right) \left| \begin{array}{l}
2\\
1
\end{array} \right.
$$
 $= \frac{{848}}{{105}}.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/06/tinh-tich-phan-bang-phuong-phap-doi-bien-so.html -->
## Ví dụ 4: Tính tích phân: $I = \int\limits_0^1 {\frac{{dx}}{{{e^{2x}} + 3}}} .$

Đặt $u = e^{2x} + 3$, suy ra $du = 2e^{2x}dx = 2(u – 3)dx$ $⇔ dx = \frac{{du}}{{2(u – 3)}}.$

Đổi cận: Với $x = 0$ thì $u = 4$, với $x = 1$ thì $u = e^2 + 3.$

Từ đó: $I = \frac{1}{2}\int\limits_4^{{e^2} + 3} {\frac{{du}}{{u(u – 3)}}}$ $= \frac{1}{6}\int\limits_4^{{e^2} + 3} {\left( {\frac{1}{{u – 3}} – \frac{1}{u}} \right)du}$ $= \frac{1}{6}\left. {\left( {\ln \left| {u – 3} \right| – \ln \left| u \right|} \right)} \right|_4^{{e^2} + 3}$ $= \frac{1}{6}\left. {\ln \left| {\frac{{u – 3}}{u}} \right|} \right|_4^{{e^2} + 3}$ $= \frac{1}{6}\ln \frac{{4{e^2}}}{{{e^2} + 3}}.$

Tính tích phân bằng phương pháp đổi biến số dạng 2
Để tính tích phân: $I = \int\limits_a^b {f(x)dx}$, với giả thiết hàm số $f(x)$ liên tục trên $[a; b]$, ta thực hiện theo các bước:

Bước 1: Chọn $x = φ(t)$, trong đó $φ(t)$ là hàm số được lựa chọn một cách thích hợp (ảnh của $φ$ nằm trong tập xác định của $f$).

Bước 2: Lấy vi phân $dx = φ'(t)dt$, giả sử $φ'(t)$ liên tục.

Bước 3: Ta lựa chọn một trong hai hướng:

+ Hướng 1: Nếu tính được các cận $α$ và $β$ tương ứng theo $a$ và $b$ (với $a = φ(α)$ và $b = φ(β)$) thì ta được: $I = \int_\alpha ^\beta {f(\varphi (t)).\varphi ‘(t)dt}.$

+ Hướng 2: Nếu không tính được dễ dàng các cận tương ứng theo $a$ và $b$ thì ta lựa chọn việc xác định nguyên hàm, từ đó suy ra giá trị của tích phân xác định (trong trường hợp này $φ$ phải là đơn ánh để diễn tả kết quả hàm số của $t$ thành hàm số của $x$).

Chú ý: Để minh hoạ việc lựa chọn một trong hai hướng trên, ta có ví dụ:

a. Với $I = \int\limits_0^{1/2} {f(x)dx}$ việc lựa chọn ẩn phụ $x = sint$, $-\frac{\pi }{2} ≤ t ≤ \frac{\pi }{2}$ cho phép ta lựa chọn hướng 1, bởi khi đó: với $x = 0$, suy ra $t = 0$, với $x = \frac{1}{2}$, suy ra $t = \frac{\pi }{6}.$

b. Với $I = \int\limits_0^{1/3} {f(x)dx}$ việc lựa chọn ẩn phụ $x = sint$, $-\frac{\pi }{2} ≤ t ≤ \frac{\pi }{2}$ ta thường lựa chọn hướng 2, bởi khi đó: với $x = \frac{1}{3}$ ta không chỉ ra được số đo góc $t$.

<!-- chunk:5 level:3 source:https://toanmath.com/2018/06/tinh-tich-phan-bang-phuong-phap-doi-bien-so.html -->
## Ví dụ 5: Tính các tích phân sau:

a. $I = \int\limits_0^{1/2} {\sqrt {1 – {x^2}} dx} .$

b. $I = \int\limits_2^{2/\sqrt 3 } {\frac{{dx}}{{x\sqrt {{x^2} – 1} }}} .$

a. Đặt $x = sint$ với $t \in \left[ { – \frac{\pi }{2}; \frac{\pi }{2}} \right]$, suy ra $dx = cost.dt.$

Đổi cận: Với $x = 0$ thì $t = 0$, với $x = \frac{1}{2}$ thì $t = \frac{\pi }{6}.$

Khi đó: $I = \int\limits_0^{\pi /6} {\sqrt {1 – {{\sin }^2}t} .\cos t.dt}$ $= \int\limits_0^{\pi /6} {{{\cos }^2}t.dt}$ $= \frac{1}{2} \int\limits_0^{\pi /6} {(1 + \cos 2t).dt}$ $= \frac{1}{2} (t + \frac{1}{2}sin2t) \left| {_0^{\pi /6}} \right.$ $= \frac{1}{2}\left( {\frac{\pi }{6} + \frac{{\sqrt 3 }}{4}} \right).$

Cách khác: Đặt $x = cost$ với $t ∈ [0; π].$

b. Đặt $x = \frac{1}{{\sin t}}$ với $t \in \left( {0; \frac{\pi }{2}} \right)$, suy ra $dx = – \frac{{\cos t.dt}}{{{{\sin }^2}t}}.$

Đổi cận: Với $x = 2$ thì $t = \frac{\pi }{6}$, với $x = \frac{2}{{\sqrt 3 }}$ thì $t = \frac{\pi }{3}.$

Khi đó: $I = \int\limits_{\pi /6}^{\pi /3} {\frac{{ – \frac{1}{{{{\sin }^2}t}}\cos tdt}}{{\frac{1}{{\sin t}}\sqrt {\frac{1}{{{{\sin }^2}t}} – 1} }}}$ $= – \int\limits_{\pi /6}^{\pi /3} {dt}$ $= – \left. t \right|_{\pi /6}^{\pi /3}$ $= – \frac{\pi }{6}.$

Cách khác: Đặt $x = \frac{1}{{co{\mathop{\rm s}\nolimits} t}}$ với $t \in \left( {0; \frac{\pi }{2}} \right).$

Chú ý:

a. Trong lời giải trên việc lựa chọn miền giá trị cho ẩn phụ $t$ phụ thuộc vào hai cận của tích phân.

b. Cũng có thể sử dụng phép đổi biến $t = \frac{1}{x}$, bằng cách viết:

$I = \int\limits_2^{2/\sqrt 3 } {\frac{{dx}}{{{x^2}\sqrt {1 – \frac{1}{{{x^2}}}} }}}$ $= \int\limits_{1/2}^{\sqrt 3 /2} {\frac{{dt}}{{\sqrt {1 – {t^2}} }}}.$

Rồi tiếp tục sử dụng phép đổi biến $t = sinu$ với $u ∈ (0; \frac{\pi }{2})$, ta được:

$I = \int\limits_{\pi /6}^{\pi /3} {du}$ $= \left. u \right|_{\pi /6}^{\pi /3}$ $= \frac{\pi }{6}.$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/06/tinh-tich-phan-bang-phuong-phap-doi-bien-so.html -->
## Ví dụ 6: Tính các tích phân sau:

a. $I = \int\limits_0^1 {x\sqrt {1 + {x^2}} dx} .$

b. $I = \int\limits_0^1 {\frac{{dx}}{{{x^2} + 1}}} .$

a. Đặt $x = tant$, $t \in \left[ { – \frac{\pi }{2}; \frac{\pi }{2}} \right]$ suy ra $dx = \frac{{dt}}{{{{\cos }^2}t}}.$

Đổi cận: Với $x = 0$ thì $t = 0$, với $x = 1$ thì $t = \frac{\pi }{4}.$

Khi đó: $I = \int\limits_0^{\pi /4} {\tan t.\sqrt {1 + {{\tan }^2}t} .\frac{{dt}}{{{{\cos }^2}t}}}$ $= – \int\limits_0^{\pi /4} {\frac{{d(\cos t)}}{{{{\cos }^4}t}}}$ $= \left. {\frac{1}{{3{{\cos }^3}t}}} \right|_0^{\pi /4}$ $= \frac{{2\sqrt 2 – 1}}{3}.$

b. Đặt $x = tant$, $t \in \left[ { – \frac{\pi }{2}; \frac{\pi }{2}} \right]$ suy ra $dx = \frac{{dt}}{{{{\cos }^2}t}}$ $= (1 + tan^{2}t)dt.$

Đổi cận: Với $x = 0$ thì $t = 0$, với $x = 1$ thì $t = \frac{\pi }{4}.$

Khi đó: $I = \int\limits_0^{\pi /4} {\frac{{(1 + {{\tan }^2}t)dt}}{{{{\tan }^2}t + 1}}}$ $= \int\limits_0^{\pi /4} {dt}$ $= {\rm{ }}t\left| {_0^{\pi /4}} \right.$ $= \frac{\pi }{4}.$

<!-- chunk:7 level:3 source:https://toanmath.com/2018/06/tinh-tich-phan-bang-phuong-phap-doi-bien-so.html -->
## Ví dụ 7: Tính các tích phân sau:

a. $I = \int\limits_{ – 1}^0 {\sqrt {\frac{{1 + x}}{{1 – x}}} dx} .$

b. $I = \int\limits_{5/4}^{3/2} {\sqrt {(x – 1)(2 – x)} dx} .$

a. Đặt $x = cos2t$, $t \in \left( {0; \frac{\pi }{2}} \right]$ suy ra $dx = -2sin2t.dt.$

Đổi cận: Với $x = -1$ thì $t = \frac{\pi }{2}$, với $x = 0$ thì $t = \frac{\pi }{4}.$

Ta có: $\sqrt {\frac{{1 + x}}{{1 – x}}} dx$ $= \sqrt {\frac{{1 + \cos 2t}}{{1 – \cos 2t}}} (-2sin2t.dt)$ $= |cott|(-2sin2t.dt)$ $= -4cos^{2}t.dt = -2(1 + cos2t)dt.$

Khi đó: $I = – 2\int\limits_{\pi /2}^{\pi /4} {(1 + \cos 2t)dt}$ $= – 2\left( {t + \frac{1}{2}\sin 2t} \right)\left| {_{\pi /2}^{\pi /4} = \frac{\pi }{2} – 1} \right.$.

b. Đặt $x = 1 + sin^{2}t$, $t \in \left[ {0; \frac{\pi }{2}} \right]$ suy ra $dx = sin2t.dt.$

Đổi cận: Với $x = \frac{5}{4}$ thì $t = \frac{\pi }{6}$, với $x = \frac{3}{2}$ thì $t = \frac{\pi }{4}.$

Ta có: $\sqrt {(x – 1)(2 – x)} dx$ $= \frac{1}{2}{\sin ^2}2tdt$ $= \frac{1}{4}\left( {1 – \cos 4t} \right)dt.$

Khi đó: $I = \int\limits_{\pi /6}^{\pi /4} {\frac{1}{4}(1 – \cos 4t)dt}$ $= \frac{1}{4}\left. {\left( {t – \frac{1}{4}\sin 4t} \right)} \right|_{\pi /6}^{\pi /4}$ $= \frac{\pi }{{48}} + \frac{{\sqrt 3 }}{{32}}.$

Phương pháp đổi biến cho lớp hàm số đặc biệt
Dựa vào việc xem xét cận của tích phân và tính chất của hàm số dưới dấu tích phân ta có thể lựa chọn phép đặt ẩn phụ, thông thường:

+ Với $I = \int\limits_{ – a}^a {f(x)dx}$ có thể lựa chọn việc đặt $x = -t.$

+ Với $I = \int\limits_0^{\pi /2} {f(x)dx}$ có thể lựa chọn việc đặt $t = \frac{\pi }{2} – x.$

+ Với $I = \int\limits_0^\pi {f(x)dx}$ có thể lựa chọn việc đặt $t = π – x.$

+ Với $I = \int\limits_0^{2\pi } {f(x)dx}$ có thể lựa chọn việc đặt $t = 2π – x.$

+ Với $I = \int\limits_a^b {xf(x)dx}$ có thể lựa chọn việc đặt $x = a + b – t.$

<!-- chunk:8 level:3 source:https://toanmath.com/2018/06/tinh-tich-phan-bang-phuong-phap-doi-bien-so.html -->
## Ví dụ 8: Tính các tích phân sau:

a. $I = \int\limits_{ – 1}^1 {{x^{2010}}\sin x.dx} .$

b. $I = \int\limits_0^{2\pi } {x.{{\cos }^3}xdx} .$

a. Viết lại $I$ dưới dạng: $I = \int\limits_{ – 1}^0 {{x^{2010}}\sin x.dx} + \int\limits_0^1 {{x^{2010}}\sin x.dx}$ $(*).$

Xét tính phân $J = \int\limits_{ – 1}^0 {{x^{2010}}\sin x.dx}$ bằng cách đặt $x = -t$ thì $dx = -dt.$

Đổi cận: Với $x = -1$ thì $t = 1$, với $x = 0$ thì $t = 0.$

Khi đó: $J = – \int\limits_1^0 {{{( – t)}^{2004}}\sin ( – t)dt}$ $= – \int\limits_0^1 {{t^{2004}}\sin tdt}$ $= – \int\limits_0^1 {{x^{2004}}\sin xdx}$ $(**).$

Thay $(**)$ vào $(*)$ ta được $I = 0.$

b. Đặt $x = 2π – t$ suy ra $dx = -dt.$

Đổi cận: Với $x = 2π$ thì $t = 0$, với $x = 0$ thì $t = 2π.$

Khi đó: $I = \int\limits_{2\pi }^0 {(2\pi – t).{{\cos }^3}(2\pi – t)( – dt)}$ $= \int\limits_0^{2\pi } {(2\pi – t).{{\cos }^3}tdt}$ $= 2\pi \int\limits_0^{2\pi } {{{\cos }^3}tdt} – \int\limits_0^{2\pi } {t{{\cos }^3}tdt}$ $= \frac{\pi }{2}\int\limits_0^{2\pi } {(\cos 3t + 3\cos t)dt} – I$ $\Leftrightarrow 2I = \frac{\pi }{2}\left( {\frac{1}{3}\sin 3t + 3\sin t} \right)\left| {_0^{2\pi } = 0} \right.$ $\Leftrightarrow I = 0.$

<!-- chunk:9 level:3 source:https://toanmath.com/2018/06/tinh-tich-phan-bang-phuong-phap-doi-bien-so.html -->
## Ví dụ 9: Tính các tích phân sau:

a. $I = \int\limits_0^\pi {x.\sin x.{{\cos }^2}} xdx.$

b. $I = \int\limits_0^{\pi /2} {\ln \left( {\frac{{1 + \sin x}}{{1 + \cos x}}} \right)} dx.$

a. Đặt $x = π – t$ suy ra $dx = -dt.$

Đổi cận: Với $x = π$ thì $t = 0$, với $x = 0$ thì $t = π.$

Khi đó: $I = – \int\limits_\pi ^0 {(\pi – t).\sin (\pi – t).{{\cos }^2}(\pi – t)dt}$ $= \int\limits_0^\pi {(\pi – t).\sin t.{{\cos }^2}tdt}$ $= \pi \int\limits_0^\pi {\sin t.{{\cos }^2}tdt}$ $– \int\limits_0^\pi {t.\sin t.{{\cos }^2}tdt}$ $= \frac{\pi }{2}\int\limits_0^\pi {\sin 2t.\cos tdt} – I$ $\Leftrightarrow 2I = \frac{\pi }{4}\int\limits_0^\pi {(\sin 3t + \sin t)dt}$ $I = \frac{\pi }{8}\left( { – \frac{1}{3}\cos 3t – \cos t} \right)\left| {_0^\pi } \right.$ $= \frac{\pi }{3}.$

b. Đặt $t = \frac{\pi }{2} – x$ suy ra $dx = -dt.$

Đổi cận: Với $x = 0$ thì $t = \frac{\pi }{2}$, với $x = \frac{\pi }{2}$ thì $t = 0.$

Khi đó: $I = \int\limits_{\pi /2}^0 {\ln \left( {\frac{{1 + \sin (\frac{\pi }{2} – t)}}{{1 + \cos (\frac{\pi }{2} – t)}}} \right)} ( – dt)$ $= \int\limits_0^{\pi /2} {\ln \left( {\frac{{1 + \cos t}}{{1 + \sin t}}} \right)} dt$ $= – \int\limits_0^{\pi /2} {\ln \left( {\frac{{1 + \sin t}}{{1 + \cos t}}} \right)} dt$ $= – \int\limits_0^{\pi /2} {\ln \left( {\frac{{1 + \sin x}}{{1 + \cos x}}} \right)} dx$ $= -I$ $⇔ 2I = 0 ⇔ I = 0.$