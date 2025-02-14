-- This is my personal Nvim configuration supporting Mac, Linux and Windows, with various plugins configured.
-- This configuration evolves as I learn more about Nvim and become more proficient in using Nvim.
-- Since it is very long (more than 1000 lines!), you should read it carefully and take only the settings that suit you.
-- I would not recommend cloning this repo and replace your own config. Good configurations are personal,
-- built over time with a lot of polish.
--
-- Author: Jiedong Hao
-- Email: jdhao@hotmail.com
-- Blog: https://jdhao.github.io/
-- GitHub: https://github.com/jdhao
-- StackOverflow: https://stackoverflow.com/users/6064933/jdhao
vim.loader.enable()

local utils = require("utils")


local expected_version = "0.10.3"
local current_version = vim.version().major .. "." .. vim.version().minor .. "." .. vim.version().patch

if current_version < expected_version then
  print("Warning: Expected version " .. expected_version .. ", but your current version is " .. current_version)
  print("Use at your own risk!")
end
local config_dir = vim.fn.stdpath("config")
---@cast config_dir string

-- some global settings
require("globals")
-- setting options in nvim
vim.cmd("source " .. vim.fs.joinpath(config_dir, "viml_conf/options.vim"))
-- various autocommands
require("custom-autocmd")
-- all the user-defined mappings
require("mappings")
-- all the plugins installed and their configurations
vim.cmd("source " .. vim.fs.joinpath(config_dir, "viml_conf/plugins.vim"))
-- colorscheme settings
require("colorschemes")
-- Ensure this command is executed after colorscheme settings
vim.cmd([[highlight Normal ctermbg=000000 guibg=000000]])
vim.opt.colorcolumn = ""
