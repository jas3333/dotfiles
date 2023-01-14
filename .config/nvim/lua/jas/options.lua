-- Line numbers
vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.numberwidth = 4

-- Tabs and indentation
vim.opt.softtabstop = 4
vim.opt.shiftwidth = 4
vim.opt.tabstop = 4
vim.opt.expandtab = true
vim.opt.autoindent = true

-- Format options
vim.api.nvim_create_autocmd("BufEnter", {
	callback = function()
		vim.opt.formatoptions = vim.opt.formatoptions - { "c", "r", "o" }
	end,
})
-- Line wrapping
vim.opt.wrap = false

-- Search settings
vim.opt.ignorecase = true
vim.opt.smartcase = true

-- Cursor
vim.opt.cursorline = true

-- Clipboard
vim.opt.clipboard:append("unnamedplus")

-- Appearance
vim.opt.termguicolors = true
vim.opt.showtabline = 2

-- Keywords
vim.opt.iskeyword:append("-")
