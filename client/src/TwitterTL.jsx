import React, { useEffect } from 'react';
//import Data from './output.json';

let Data = {};


const TwitterTL = ()=>{
    fetch('http://127.0.0.1:8000/home/?access_token=&access_token_secret=', {
        method:'get'
    }).then((data) => {
        return data.json();
    }).then((data) => {
        console.log("--- data ---");
        console.log(data);
        Data = data;
        //completeAssign(Data, data);
    });

    console.log("--- Data ---");
    console.log(Data);
    return (
        <div className='TTL_wr'>
            {Data.data ? Data.data.map(v=>{
                let u_index = GetUser(v.author_id);
                let u_name;
                let u_username;
                let u_icon;
                if(u_index < 0){
                    u_name = "unknown";
                    u_username = "unknown";
                    u_icon = "https://pbs.twimg.com/profile_images/1582551294262534144/P09lQPRe_400x400.jpg";
                }
                else{
                    u_name = Data.includes.users[u_index].name;
                    u_username = Data.includes.users[u_index].username;
                    u_icon = Data.includes.users[u_index].profile_image_url;
                }
                let photo_srcs = [];
                if(v.attachments){
                    v.attachments.media_keys.forEach(
                        mk => {
                            let m_index = GetMedia(mk);
                            if(m_index < 0)return;
                            switch(Data.includes.media[m_index].type){
                                case "photo":
                                    photo_srcs.push(Data.includes.media[m_index].url || "");
                                    break;
                            }
                        }
                    );
                }
                return (
                <div key={v.id} className="p_parts" style={{background: "white"}}>
                    <p className="p_parts_id" style={{fontSize:"15px", verticalAlign:"middle"}}>
                        <img
                            src={u_icon}
                            style={{
                                width: "30px",
                                borderRadius: "50%",
                                verticalAlign: "middle"
                            }}
                        />
                        <span style={{verticalAlign:"middle"}}> {u_name} </span>
                        <span style={{fontSize:"80%", color:"gray"}}>{"@"+u_username}</span>
                    </p>
                    <div className="p_parts_text" style={{margin: 0}}>
                        {
                            (()=>{
                                let rtn = [];
                                //let rtn:(string|React.DetailedHTMLProps<React.AnchorHTMLAttributes<HTMLAnchorElement>, HTMLAnchorElement>)[] = [];
                                let txt = v.text;
                                let txts;
                                let atags = [];
                                let mch = txt.match(/http(s)?:\/\/([\w-]+\.)+[\w-]+(\/[\w- ./?%&=]*)?/g);
                                if(0 && mch){
                                    // URLを含む
                                    txts = txt.split(/http(s)?:\/\/([\w-]+\.)+[\w-]+(\/[\w- ./?%&=]*)?/g);
                                    mch.forEach(str=>{
                                        atags.push((
                                            <a key={str} href={str}>{str}</a>
                                        ));
                                    });
                                    for(let i=0; i<txts.length; i++){
                                        //
                                        rtn.push(<span>{txts[i]}</span>);
                                        if(i<txts.length-1)rtn.push(atags[i]);
                                    }
                                    return (
                                        <div>{0}</div>
                                    );
                                }
                                else{
                                    return (
                                        <div>{v.text}</div>
                                    );
                                }
                            })()
                        }
                        {photo_srcs.map(src=>(
                            <img key={src} src={src} style={{width:"100%"}}/>
                        ))}
                        <div style={{
                            textAlign: "right",
                            fontSize: "10px",
                            color: "gray"
                        }}>
                            {v.created_at}
                        </div>
                    </div>
                    <p className="p_parts_mtx" style={{margin:0}}>
                        ↩{v.public_metrics.reply_count}
                        　≫{v.public_metrics.quote_count}
                        　RT {v.public_metrics.retweet_count}
                        　❤{v.public_metrics.like_count}
                    </p>
                </div>
                );
            }) : null}
            
        </div>
    );
}

function GetUser(author_id){
    return Data.includes.users.findIndex(e=>e.id==author_id);
}

function GetMedia(media_key){
    return Data.includes.media.findIndex(e=>e.media_key==media_key);
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

export default TwitterTL;