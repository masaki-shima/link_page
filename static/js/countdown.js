// 目標日時を指定（年, 月（0-11）, 日, 時, 分, 秒）
// const targetDate = new Date( 2024, 7, 26, 22, 0, 0 );
// 以下のように文字列型の日付フォーマットの指定でもOK
const targetDate = new Date( '2024/9/24 22:00:00' );

 
// カウントダウンタイマー
const ele = document.getElementById( 'countdown' );
 
// カウントダウン処理
const countdown = () => {
  // 現在日時
  const now = new Date();
  // 時差
  const distance = targetDate - now;
 
  if ( distance < 0 ) {
    ele.innerHTML = "カウントダウン終了！(DBリセット)";
 
  } else {
    const days = Math.floor( distance / ( 1000 * 60 * 60 * 24 ) );
    const hours = Math.floor( ( distance % ( 1000 * 60 * 60 * 24 ) ) / ( 1000 * 60 * 60 ) );
    const minutes = Math.floor( ( distance % ( 1000 * 60 * 60 ) ) / ( 1000 * 60 ) );
    const seconds = Math.floor( ( distance % ( 1000 * 60 ) ) / 1000 );
    const miliseconds = distance < 0 ? 0 : Math.floor( distance % 1000 );
 
    // カウントダウンタイマーのHTML更新
    ele.innerHTML = `DBリセットまであと↓<br /><span class="days">${ days }</span>日と<span class="hours">${ String( hours ).padStart( 2, '0' ) }</span>時間<span class="minutes">${ String( minutes ).padStart( 2, '0' ) }</span>分<span class="seconds">${ String( seconds ).padStart( 2, '0' ) }</span>.${ String( miliseconds ).padStart( 3, '0' ) }秒`;
 
    // 再度タイマー更新の実行
    window.requestAnimationFrame( countdown );
  }
}
 
// カウントダウンタイマーの起動
window.requestAnimationFrame( countdown );
