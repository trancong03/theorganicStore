import { Search } from 'lucide-react'
import React from 'react'

export default function Header() {
  return (
      <div className=' h-[10vh] relative  flex bg-white justify-between items-center p-3'>
          <div className="absolute left-1/2 transform -translate-x-1/2">
              <img className='h-12 sm:h-8 md:h-10 lg:h-16 w-auto' src='https://theciu.vn/img/logo-dark.png' alt='The CIU Logo' />
          </div>
          <div className="hidden lg:flex items-center border-b border-gray-300 py-2 ml-auto">
              <button>
                  <Search />
              </button>
              <input
                  className="ml-2 w-80 border-none focus:outline-none placeholder-gray-500 text-gray-700"
                  type="text"
                  placeholder="Tìm sản phẩm..."
              />
          </div>
    </div>
  )
}
