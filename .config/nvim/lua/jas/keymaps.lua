local options = { noremap = true, silent = true }
local term_options = { silent = true }

-- Shorten vim function
local keymap = vim.api.nvim_set_keymap

keymap("", "<space>", "<Nop>", options)
vim.g.mapleader = " "
vim.g.maplocalleader = " "

-- Better window navigation
keymap("n", "<C-h>", "<C-w>h", options)
keymap("n", "<C-j>", "<C-w>j", options)
keymap("n", "<C-k>", "<C-w>k", options)
keymap("n", "<C-l>", "<C-w>l", options)

-- Window Resizing
keymap("n", "<C-Up>", ":resize +2<CR>", options)
keymap("n", "<C-Down>", ":resize -2<CR>", options)
keymap("n", "<C-Left>", ":vertical resize -2<CR>", options)
keymap("n", "<C-Right>", ":vertical resize +2<CR>", options)

-- Change buffers
keymap("n", "<S-l>", ":bnext<CR>", options)
keymap("n", "<S-h>", ":bprevious<CR>", options)

keymap("n", "<Space>1", ":BufferGoto 1<CR>", options)
keymap("n", "<Space>2", ":BufferGoto 2<CR>", options)
keymap("n", "<Space>3", ":BufferGoto 3<CR>", options)
keymap("n", "<Space>4", ":BufferGoto 4<CR>", options)
keymap("n", "<Space>5", ":BufferGoto 5<CR>", options)
keymap("n", "<Space>6", ":BufferGoto 6<CR>", options)
keymap("n", "<Space>7", ":BufferGoto 7<CR>", options)
keymap("n", "<Space>8", ":BufferGoto 8<CR>", options)
keymap("n", "<Space>9", ":BufferGoto 9<CR>", options)

--Copilot
vim.cmd([[imap <silent><script><expr> <C-a> copilot#Accept("\<CR>")]])
vim.g.copilot_no_tab_map = true

-- Stay in indent mode
keymap("v", "<", "<gv", options)
keymap("v", ">", ">gv", options)

-- Quick escape from insert mode
keymap("i", "jj", "<ESC>", options)

-- Nvim-Tree
keymap("n", "<leader>e", ":NvimTreeToggle<CR>", options)

-- Telescope
keymap("n", "<leader>f", "<cmd>Telescope find_files<cr>", options) -- find files within current working directory
keymap("n", "<leader>g", "<cmd>Telescope live_grep<cr>", options) -- find string in current working directory as you type
--keymap("n", "<leader>fc", "<cmd>Telescope grep_string<cr>", options) -- find string under cursor in current working directory

-- Comment Box
keymap("n", "<leader>ac", "<cmd>lua require('comment-box').cbox()<CR>", options)
keymap("v", "<leader>ac", "<cmd>lua require('comment-box').cbox()<CR>", options)
