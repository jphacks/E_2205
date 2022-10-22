import _Data from './output.json';

let data = [];
_Data.data.forEach(u=>{
    u.forEach(v=>{
        data.push(v);
    })
})
data.forEach(v=>{
    //             0  1  2  3  4  5
    // example: 2022-06-23 07:26:53+00:00
    let d = v.date.split(/\D+/g).map(d=>+d);
    v._date_ = new Date(d[0], d[1], d[2], d[3], d[4], d[5]);
});
data.sort((a,b)=>{
    return b._date_ - a._date_;
})

const InstagramTL = ()=>{
    return (
        <div className='TTL_wr'>
            {data.map(v=>{
                let photo_srcs = v.media;
                console.log(photo_srcs);
                return (
                <div key={v.date} className="p_parts" style={{background: "white"}}>
                    <p className="p_parts_id" style={{fontSize:"15px", verticalAlign:"middle"}}>
                        <span style={{verticalAlign:"middle"}}> {v.user} </span>
                    </p>
                    <div className="p_parts_text" style={{margin: 0}}>
                        <div>{v.text}</div>
                        {photo_srcs.map(src=>(
                            <a href={src} key={src} style={{marginRight: "10px"}}>◇</a>
                        ))}
                        <div style={{
                            textAlign: "right",
                            fontSize: "10px",
                            color: "gray"
                        }}>
                            {v.date}
                        </div>
                    </div>
                    <p className="p_parts_mtx" style={{margin:0}}>
                        　❤{v.like}
                    </p>
                </div>
                );
            })}
            
        </div>
    );
}


// オブジェクトの完全コピー
function completeAssign(target, ...sources) {
    sources.forEach(source => {
      let descriptors = Object.keys(source).reduce((descriptors, key) => {
        descriptors[key] = Object.getOwnPropertyDescriptor(source, key);
        return descriptors;
      }, {});
  
      // 既定では、 Object.assign は列挙可能なシンボルもコピーする
      Object.getOwnPropertySymbols(source).forEach(sym => {
        let descriptor = Object.getOwnPropertyDescriptor(source, sym);
        if (descriptor.enumerable) {
          descriptors[sym] = descriptor;
        }
      });
      Object.defineProperties(target, descriptors);
    });
    return target;
  }

export default InstagramTL;