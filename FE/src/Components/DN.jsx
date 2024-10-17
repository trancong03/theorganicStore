import React, { useEffect, useState, useRef } from 'react';
import '../Style/login.css';
import { FaFacebookF, FaGooglePlusG } from 'react-icons/fa';
import { BadgeX } from 'lucide-react';

const DN = ({ closeLogin, onLoginSuccess }) => {
    const [isRightPanelActive, setIsRightPanelActive] = useState(false);
    const formRef = useRef(null);
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false); // Thêm state loading

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!username || !password) {
            setError("Username và Password không được để trống.");
            return;
        }
        const usernameRegex = /^[a-zA-Z0-9_]+$/;
        if (!usernameRegex.test(username)) {
            setError("Username chỉ được chứa chữ cái, số và dấu gạch dưới.");
            return;
        }
        if (password.length < 5) {
            setError("Password phải có ít nhất 5 ký tự.");
            return;
        }
        setError(""); // Xóa lỗi trước khi gửi
        setLoading(true); // Bật chế độ loading
        try {
            const response = await fetch('http://127.0.0.1:8000/api/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });
            if (!response.ok) {
                throw new Error('Thông tin xác thực không hợp lệ');
            }
            const data = await response.json();
            onLoginSuccess(data);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false); // Tắt chế độ loading
        }
    };

    const handleSignUpClick = () => {
        setIsRightPanelActive(true);
    };

    const handleSignInClick = () => {
        setIsRightPanelActive(false);
    };

    useEffect(() => {
        const handleClickOutside = (event) => {
            if (formRef.current && !formRef.current.contains(event.target)) {
                closeLogin(); // Đóng form nếu nhấn ra ngoài
            }
        };
        document.addEventListener("mousedown", handleClickOutside);
        return () => {
            document.removeEventListener("mousedown", handleClickOutside);
        };
    }, [closeLogin]);

    return (
        <div className='login-container fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50'>
            <div
                className={`container ${isRightPanelActive ? 'right-panel-active' : ''}`}
                id="container"
                ref={formRef}
            >
                {/* Nút đóng (X) */}
                <button className="close-button " onClick={closeLogin}>
                    <BadgeX className="w-8 h-8" />
                </button>

                <div className="form-container sign-up-container">
                    <form>
                        <img
                            className="h-12 sm:h-8 md:h-10 lg:h-16 w-auto"
                            src="/image/logo.png"
                            alt="The CIU Logo"
                        />
                        <h1>Create Account</h1>
                        <div className="social-container">
                            <a href="#" className="social"><FaFacebookF /></a>
                            <a href="#" className="social"><FaGooglePlusG /></a>
                        </div>
                        <span>or use your email for registration</span>
                        <input type="text" placeholder="Username" />
                        <input type="password" placeholder="Password" />
                        <button>Sign Up</button>
                    </form>
                </div>

                <div className="form-container sign-in-container">
                    {/* Nút đóng (X) */}
                    <button className="close-button " onClick={closeLogin}>
                        <BadgeX className="w-8 h-8" />
                    </button>

                    <form onSubmit={handleSubmit} method='POST'>
                        <img
                            className="h-12 sm:h-8 md:h-10 lg:h-16 w-auto"
                            src="/image/logo.png"
                            alt="The CIU Logo"
                        />
                        <h1>Sign in</h1>
                        <div className="social-container">
                            <a href="#" className="social"><FaFacebookF /></a>
                            <a href="#" className="social"><FaGooglePlusG /></a>
                        </div>
                        <span>or use your account</span>
                        <input type="text" placeholder="Username"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)} />
                        <input type="password"
                            placeholder="Password" value={password}
                            onChange={(e) => setPassword(e.target.value)} />
                        <span className='text-red-600'>
                            {error && <p className="error">{error}</p>}
                        </span>
                        <a href="#">Forgot your password?</a>
                        <button type="submit" disabled={loading}> {/* Disable button khi loading */}
                            {loading ? 'Đang đăng nhập...' : 'Sign In'} {/* Hiển thị thông điệp loading */}
                        </button>
                    </form>
                </div>

                <div className="overlay-container">
                    <div className="overlay  bg-slate-500/50">
                        <div className="overlay-panel overlay-left  bg-slate-500/50">
                            <h1>Welcome Back!</h1>
                            <p>To keep connected with us please login with your personal info</p>
                            <button className="ghost" id="signIn" onClick={handleSignInClick}>Sign In</button>
                        </div>
                        <div className="overlay-panel overlay-right  bg-slate-500/50">
                            <h1>Hello!</h1>
                            <p>Enter your personal details and start journey with us</p>
                            <button className="ghost" id="signUp" onClick={handleSignUpClick}>Sign Up</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default DN;
