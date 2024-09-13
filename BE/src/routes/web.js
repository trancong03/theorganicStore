const express = require('express');
const router = express.Router();
const { getHomepage, getAboutHome } = require('../controllers/homeController')

router.get('/', getHomepage)

router.get('/about',getAboutHome)

module.exports = router; // export defaultS