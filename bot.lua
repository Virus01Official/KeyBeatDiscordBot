local discordia = require('discordia')
local client = discordia.Client()

-- Define the announcement role IDs
local ANNOUNCEMENT_ROLE_ID = 1208379129523605584
local LEAKS_ROLE_ID = 1208379179134091334

client:on('messageCreate', function(message)
    if message.author == client.user then return end

    -- Command: !feedback
    if message.content:match('^!feedback ') then
        local feedback = message.content:sub(10) -- Extract feedback text
        local feedback_channel = client:getChannel(1262021731292418119) -- Replace with your feedback channel ID

        if feedback_channel then
            feedback_channel:send("New feedback from " .. message.author.mentionString .. ":\n" .. feedback)
            message.channel:send("Thank you for your feedback! It has been submitted.")
        else
            message.channel:send("Feedback channel not found. Please set up a valid feedback channel.")
        end

    -- Command: !announce
    elseif message.content:match('^!announce ') and message.member:hasRole(ANNOUNCEMENT_ROLE_ID) then
        local content = message.content:sub(10) -- Extract command content
        local args = content:match("^(.-) (.+)$") -- Split into channel and message
        if args then
            local channel_id, msg = args:match("^(%d+) (.+)$")
            local channel = client:getChannel(tonumber(channel_id))
            local announcement_role = message.guild:getRole(ANNOUNCEMENT_ROLE_ID)

            if channel then
                if announcement_role then
                    channel:send(announcement_role.mentionString .. " " .. msg)
                    message.channel:send("Announcement has been sent.")
                else
                    message.channel:send("Announcement role not found. Please set up a valid role.")
                end
            else
                message.channel:send("Announcement channel not found. Please set up a valid channel.")
            end
        else
            message.channel:send("Invalid command format. Use !announce <channel_id> <message>")
        end

    -- Command: !leaks
    elseif message.content:match('^!leaks ') and message.member:hasRole(LEAKS_ROLE_ID) then
        local content = message.content:sub(7) -- Extract command content
        local announcement_channel = client:getChannel(1208377063870824458) -- Replace with your leaks channel ID
        local announcement_role = message.guild:getRole(LEAKS_ROLE_ID)

        if announcement_channel then
            if announcement_role then
                announcement_channel:send(announcement_role.mentionString .. " " .. content)
                message.channel:send("Announcement has been sent.")
            else
                message.channel:send("Announcement role not found. Please set up a valid role.")
            end
        else
            message.channel:send("Announcement channel not found. Please set up a valid announcement channel.")
        end
    end
end)

client:run('Bot [TOKEN]')
