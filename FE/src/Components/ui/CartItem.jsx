export default function CartItem({ name, price, images = [], onAddToCart }) {
  const defaultImage = 'default.jpg';

  const handleAddToCart = () => {
    onAddToCart(); // Call the passed function
  };

  return (
    <div className='w-[15vw] bg-[#f3f3f3] rounded-2xl ml-3 mb-5 group'>
      <div className='relative overflow-hidden flex items-center justify-center flex-col'>
        <img 
          src={`image/${images.length > 0 ? images[0] : defaultImage}`} 
          alt={name} 
          className='w-[18rem] h-[22rem] rounded-xl' 
        />
        <div className='absolute h-full w-full bg-black/60 rounded-2xl flex flex-col items-center justify-between p-5 -bottom-10 group-hover:bottom-0 opacity-0 group-hover:opacity-100 transition-all duration-300'>
          <div className='text-center'>
            <h3 className='line-clamp-3 font-arial text-white text-xl'>{name || 'Sản phẩm không có tên'}</h3>
            <p className='text-lg font-bold text-white text-xl'>
              Giá: {price || 0}<span>đ</span>
            </p>
          </div>
          <button 
            className='w-[10rem] h-[3rem] bg-[#1D7E20] text-white font-bold rounded-full mt-auto'
            onClick={handleAddToCart} 
          >
            Thêm giỏ hàng
          </button>
        </div>
      </div>
    </div>
  );
}
