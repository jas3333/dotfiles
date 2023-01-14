local saga_status, saga = pcall(require, "lspsaga")
if not saga_status then
	return
end

require("lspsaga").init_lsp_saga({})

-- saga.init_lsp_saga({
--     move_in_saga = {prev = "<C-K>", next = "<C-J>" },
--     finder_action_keys = {
--         open = "<CR>",
--     },
--     definition_action_keys = {
--         edit = "<CR>",
--     },
-- })
