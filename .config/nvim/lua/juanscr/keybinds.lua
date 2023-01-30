-- Leader
vim.g.mapleader = " "

-- File related stuf
vim.keymap.set("n", "<leader>fe", vim.cmd.Ex)

-- Move files in visual mode
vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv")
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv")

-- Paste without replacing
vim.keymap.set("x", "<leader>p", "\"_dP")
