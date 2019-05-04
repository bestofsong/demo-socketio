const _ = require('lodash')
const server = require('http').createServer()
const io = require('socket.io')(server)

const PORT = 5000
const nsp = '/demo'

io
  .of(nsp)
  .on('connect',
    client => {
      client.on('message', (...data) => {
        console.log('%s: message: ', client.id, data)
        const ack = _.last(data)
        if (typeof ack === 'function') {
          ack(`roger(${client.id})`)
        }
      })
      client.on('my message', (...data) => {
        console.log('%s: my message: ', client.id, data)
        const ack = _.last(data)
        if (typeof ack === 'function') {
          ack(`roger(${client.id})`)
        }
      })
      client.on('disconnect', () => {
        console.log('%s: disconnect', client.id)
      })
    })
server.listen(PORT)
