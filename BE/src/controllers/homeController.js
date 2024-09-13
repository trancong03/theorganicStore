const getHomepage =(req ,res)=>{
    res.send('Hello World! Tôi là Công đây ')
}
const getAboutHome = (req, res) => {
    res.render('sample.ejs')// Tự động render ra giao diện
}
module.exports = {
    getHomepage,
    getAboutHome
} // export object